# Experimental FM Synthesizer

Experimental frequency modulation (FM) synthesizer to experiment with the ideas expressed in the [John Chowning, Computer Music, DX7 & FM Discovery](https://www.youtube.com/watch?v=Mu8lHX-xuSg) video by Anthony Marinelli Music.

[![Watch the video](https://img.youtube.com/vi/Mu8lHX-xuSg/0.jpg)](https://www.youtube.com/watch?v=Mu8lHX-xuSg)

To some people, frequency modulation as implemented in the DX series of synthesizers (using algorithms) is complex to grasp. When asked, John Chowning, the discoverer of frequency modulation, gave an explanation how he uses it - and it is very different from how it is implemented in the DX series of synthesizers:

> Chowning: FM is two carriers and one modulator. It's my basic unit. And then the complexity is by adding bunches of those. It's the idea of two oscillators, and complexity is by putting a lot of those together. 
> 
> Marinelli: So just one modulator, and then the carriers can be whatever. 
> 
> Chowning: If you have two carriers, you can create resonances, a simulation of resonances like more vocal tones.
> 
> So you have one carrier that modulates the pitch frequency, and the other one is a multiple of the pitch frequency. So if you want a resonance around the seventh harmonic, you make that carrier seven times the pitch with a separate envelope. The modulator is the same for both; the modulator is always the pitch frequency. So that's my basic unit, and complexity then is just multiple (of those).
> 
> Marinelli: Yeah, I mean, I get that because by limiting, you can work with it. It's like starting with an orchestra. It's like, okay, there's a violin, and then I know how to do things to go off the rails and play the violin in all these different parts: col legno, sul tasto, going crazy and creating sidebands with them beating against each other and all that. But there's still a core that you want to come home to as the listener of your own music, too. There's not just the listener out there to follow your own flow. So I like what you're saying. It shows me a lot that you, who can have all this unlimited amount of possibilities, still come home to something and build from there.

Source: [John Chowning, Computer Music, DX7 & FM Discovery](https://www.youtube.com/watch?v=Mu8lHX-xuSg), slightly abridged

So, **multiple units containing two carriers and one modulator each**. This is how John Chowning, the discoverer of frequency modulation, uses it.

## Features

- **Multiple Synth Instances**: Up to 8 synthesizers can be added, each on its own tab.
- **FM Synthesis**: Create sounds using two carriers and one modulator.
- **ADSR Envelope Control**: Adjust Attack, Decay, Sustain, and Release parameters for each operator.
- **Volume Control**: Individual volume control for each synthesizer and an overall volume control.
- **Written in Python**: Easily change how the synthesizer works.

## Installation

To run this project, you'll need Python 3 and the required dependencies. 

```
git clone https://github.com/probonopd/ExperimentalFMSynth/
cd ExperimentalFMSynth
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

## Usage

Run the main script to start the synthesizer application:

```
python ExperimentalFMSynth.py
```

## Acknowledgments

- [John Chowning, Computer Music, DX7 & FM Discovery](https://www.youtube.com/watch?v=Mu8lHX-xuSg) for insights into FM synthesis.
- [Anthony Marinelli Music](https://www.youtube.com/watch?v=Mu8lHX-xuSg) for the educational video.

## Contributing

Feel free to fork the repository, create a branch, and submit a pull request with your changes.
