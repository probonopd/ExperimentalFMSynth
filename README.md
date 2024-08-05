# Experimental FM Synthesizer

Experimental frequency modulation (FM) synthesizer to experiment with the ideas expressed in the [John Chowning, Computer Music, DX7 & FM Discovery](https://www.youtube.com/watch?v=Mu8lHX-xuSg) video by Anthony Marinelli Music.

[![Watch the video](https://img.youtube.com/vi/Mu8lHX-xuSg/0.jpg)](https://www.youtube.com/watch?v=Mu8lHX-xuSg)

To some people, frequency modulation as implemented in the DX series of synthesizers (using algorithms) is complex to grasp. When asked, John Chowning, the discoverer of frequency modulation, gave an explanation how he uses it - and it is very different from how it is implemented in the DX series of synthesizers:

> Chowning: FM is two carriers and one modulator. It's my basic unit. And then the complexity is by adding bunches of those. It's the idea of two oscillators, and complexity is by putting a lot of those together. 
> 
> Marinelli: So just one modulator, and then the carriers can be whatever. 
> 
> Chowning: If you have two carriers, you can create resonances, a simulation of resonances like more vocal tones. So you have one carrier that modulates the pitch frequency, and the other one is a multiple of the pitch frequency. So if you want a resonance around the seventh harmonic, you make that carrier seven times the pitch with a separate envelope. The modulator is the same for both; the modulator is always the pitch frequency. So that's my basic unit, and complexity then is just multiple (of those).

Source: [John Chowning, Computer Music, DX7 & FM Discovery](https://www.youtube.com/watch?v=Mu8lHX-xuSg), slightly abridged

So, **multiple units containing two carriers and one modulator each**. This is how John Chowning, the discoverer of frequency modulation, uses it.

## Screenshot

![image](https://github.com/user-attachments/assets/9a0a343a-c293-4d79-bbb9-dbe897e391d1)

## Features

- **Multiple Synth Instances**: Up to 8 synthesizers can be added, each on its own tab.
- **FM Synthesis**: Create sounds using two carriers and one modulator.
- **ADSR Envelope Control**: Adjust Attack, Decay, Sustain, and Release parameters for each operator.
- **Volume Control**: Individual volume control for each synthesizer and an overall volume control.
- **Written in Python**: Easily change how the synthesizer works.

## Download

Portable application that can run without needing to be installed: [Download for Windows, Mac, and Linux](https://github.com/probonopd/ExperimentalFMSynth/releases/tag/continuous)

## Installation

If you just want to run the application without installing anything, use the donwnload provided above. If you are a developer and would like to edit the code, you'll need Python 3 and the required dependencies. 

```
git clone https://github.com/probonopd/ExperimentalFMSynth/
cd ExperimentalFMSynth
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

Run the main script to start the synthesizer application:

```
python ExperimentalFMSynth.py
```

## Contributing

Feel free to fork the repository, create a branch, and submit a pull request with your changes.

### TODO

Pull requests that implement the following are especially welcome:

- [ ] Bugfixes
- [ ] More concepts from the video applied to code, e.g.,
  - [ ] Slider for frequency of carrier 2 should adjust multiples of frequency of carrier 1 ("So you have one carrier that modulates the pitch frequency, and the other one is a multiple of the pitch frequency")
  - [ ] If the frequency of carrier 1 changes, make the frequency of the modulator change accordingly, but not the other way around ("The modulator is always the pitch frequency")
- [ ] Add a way to play MIDI files with this synth
- [ ] Turn into a VST3

## Acknowledgments

- [John Chowning, Computer Music, DX7 & FM Discovery](https://www.youtube.com/watch?v=Mu8lHX-xuSg) for insights into FM synthesis.
- [Anthony Marinelli Music](https://www.youtube.com/watch?v=Mu8lHX-xuSg) for the educational video.
