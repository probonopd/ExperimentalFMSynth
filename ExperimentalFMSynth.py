#!/usr/bin/env python3

import sys
import numpy as np
import sounddevice as sd
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QGroupBox, QPushButton, QSlider, QLabel, QHBoxLayout, QCheckBox, QLineEdit
from PyQt6.QtCore import QThread, pyqtSignal, Qt, QTimer

class AudioThread(QThread):
    signal_play = pyqtSignal()

    def __init__(self, synth):
        super().__init__()
        self.synth = synth
        self.playing = False

    def run(self):
        while self.playing:
            signal = self.synth.generate_fm_signal()
            sd.play(signal, samplerate=44100)
            sd.wait()

    def start_playing(self):
        self.playing = True
        if not self.isRunning():
            self.start()

    def stop_playing(self):
        self.playing = False
        self.wait()

class FMSynth(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("FM Synthesizer")
        self.setGeometry(100, 100, 400, 600)
        self.layout = QVBoxLayout()

        self.carrier1_group, self.carrier1_sliders, self.carrier1_checkbox = self.create_operator_group("Carrier 1", 440, 100, 100, 70, 100, 100, 100)
        self.carrier2_group, self.carrier2_sliders, self.carrier2_checkbox = self.create_operator_group("Carrier 2", 660, 100, 100, 70, 100, 100, 100)
        self.modulator_group, self.modulator_sliders, self.modulator_checkbox = self.create_operator_group("Modulator", 5, 100, 100, 70, 100, 100, 100)

        for group in [self.carrier1_group, self.carrier2_group, self.modulator_group]:
            self.layout.addWidget(group)

        self.volume_slider = self.create_slider("Volume (%)", 25, self.update_volume)
        self.freq_ratio_label = QLabel("Volume: 25%")
        self.layout.addWidget(self.freq_ratio_label)

        self.play_button = QPushButton("Play")
        self.play_button.clicked.connect(self.toggle_play)
        self.layout.addWidget(self.play_button)

        self.setLayout(self.layout)
        self.audio_thread = AudioThread(self)
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_sound)

    def create_operator_group(self, title, *params):
        group = QGroupBox(title)
        layout = QVBoxLayout()
        labels = ["Frequency (Hz)", "Attack (ms)", "Decay (ms)", "Sustain (%)", "Release (ms)", "Amount (%)"]
        sliders = []
        edits = []
        checkbox = QCheckBox("Enable")
        checkbox.setChecked(True)

        for i, label in enumerate(labels):
            slider = QSlider(Qt.Orientation.Horizontal)
            if i == 0:  # Frequency
                slider.setRange(100, 2000)
            elif i < 3:  # Attack, Decay
                slider.setRange(0, 2000)
            else:  # Sustain, Release, Amount
                slider.setRange(0, 100)
            slider.setValue(params[i])
            slider.setFixedWidth(200)

            edit = QLineEdit(str(params[i]))
            edit.setFixedWidth(50)

            slider.valueChanged.connect(lambda value, e=edit: e.setText(str(value)))
            edit.textChanged.connect(lambda text, s=slider: self.set_slider_value(s, text))
            
            layout.addLayout(self.create_hbox(label, slider, edit))
            sliders.append(slider)
            edits.append(edit)

        layout.addWidget(checkbox)
        group.setLayout(layout)
        return group, sliders, checkbox

    def create_hbox(self, label, slider, widget):
        hbox = QHBoxLayout()
        hbox.addWidget(QLabel(label))
        hbox.addWidget(slider)
        hbox.addWidget(widget)
        return hbox

    def create_slider(self, label, value, callback):
        slider = QSlider(Qt.Orientation.Horizontal)
        slider.setRange(0, 100)
        slider.setValue(value)
        slider.valueChanged.connect(callback)
        layout = QHBoxLayout()
        layout.addWidget(QLabel(label))
        layout.addWidget(slider)
        self.layout.addLayout(layout)
        return slider

    def set_slider_value(self, slider, text):
        if text.isdigit():
            value = int(text)
            if 0 <= value <= slider.maximum():
                slider.setValue(value)

    def update_volume(self):
        self.freq_ratio_label.setText(f"Volume: {self.volume_slider.value()}%")

    def update_sound(self):
        if self.audio_thread.isRunning():
            self.audio_thread.signal_play.emit()

    def generate_adsr_envelope(self, duration, attack, decay, sustain, release, amount, sample_rate=44100):
        total_samples = int(sample_rate * duration)
        envelope = np.zeros(total_samples)

        attack_samples = int(sample_rate * (attack / 1000))
        decay_samples = int(sample_rate * (decay / 1000))
        sustain_level = sustain / 100

        envelope[:attack_samples] = np.linspace(0, 1, attack_samples)
        envelope[attack_samples:attack_samples + decay_samples] = np.linspace(1, sustain_level, decay_samples)

        sustain_samples = total_samples - (attack_samples + decay_samples + int(sample_rate * (release / 1000)))
        envelope[attack_samples + decay_samples:attack_samples + decay_samples + sustain_samples] = sustain_level

        release_samples = int(sample_rate * (release / 1000))
        envelope[attack_samples + decay_samples + sustain_samples:] = np.linspace(sustain_level, 0, release_samples)

        envelope *= (amount / 100)  # Scale envelope by the amount

        return envelope

    def generate_fm_signal(self, duration=2.0, sample_rate=44100):
        carrier1_freq = self.carrier1_sliders[0].value()
        carrier2_freq = self.carrier2_sliders[0].value()
        modulator_freq = self.modulator_sliders[0].value()
        carrier1_modulation_index = self.modulator_sliders[1].value() / 100
        carrier2_modulation_index = self.modulator_sliders[2].value() / 100

        carrier1_enabled = self.carrier1_checkbox.isChecked()
        carrier2_enabled = self.carrier2_checkbox.isChecked()
        modulator_enabled = self.modulator_checkbox.isChecked()

        carrier1_envelope = self.generate_adsr_envelope(duration, self.carrier1_sliders[1].value(), self.carrier1_sliders[2].value(), self.carrier1_sliders[3].value(), self.carrier1_sliders[4].value(), self.carrier1_sliders[5].value())
        carrier2_envelope = self.generate_adsr_envelope(duration, self.carrier2_sliders[1].value(), self.carrier2_sliders[2].value(), self.carrier2_sliders[3].value(), self.carrier2_sliders[4].value(), self.carrier2_sliders[5].value())
        modulator_envelope = self.generate_adsr_envelope(duration, self.modulator_sliders[1].value(), self.modulator_sliders[2].value(), self.modulator_sliders[3].value(), self.modulator_sliders[4].value(), self.modulator_sliders[5].value())

        t = np.arange(0, duration, 1 / sample_rate)
        modulator_signal = np.sin(2 * np.pi * modulator_freq * t) * modulator_envelope if modulator_enabled else np.zeros(len(t))
        carrier1_signal = np.sin(2 * np.pi * carrier1_freq * t + carrier1_modulation_index * modulator_signal) * carrier1_envelope if carrier1_enabled else np.zeros(len(t))
        carrier2_signal = np.sin(2 * np.pi * carrier2_freq * t + carrier2_modulation_index * modulator_signal) * carrier2_envelope if carrier2_enabled else np.zeros(len(t))

        signal = carrier1_signal + carrier2_signal
        signal = signal / np.max(np.abs(signal)) if np.max(np.abs(signal)) != 0 else np.zeros(len(t))

        volume = self.volume_slider.value() / 100
        signal *= volume
        
        return signal

    def toggle_play(self):
        if self.audio_thread.isRunning():
            self.audio_thread.stop_playing()
            self.play_button.setText("Play")
            self.timer.stop()
        else:
            self.audio_thread.start_playing()
            self.play_button.setText("Stop")
            self.timer.start(100)

    def closeEvent(self, event):
        self.audio_thread.stop_playing()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    synth = FMSynth()
    synth.show()
    sys.exit(app.exec())
