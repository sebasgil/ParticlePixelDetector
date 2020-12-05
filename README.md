# ParticlePixelDetector

## Example usage
```python
# 1. Setup
# a detector geometry, passed to all components as configuration
geometry = common.DetectorGeometry()
# initialize a new event generator
event_generator = simulation.EventGenerator(geometry)
# initialize a new event reconstructor
reconstructor = reconstruction.Reconstructor(geometry)

# 2. Fun :)
# generate a single event
event = event_generator.get_random_event()
# reconstruct the originial path
path = reconstructor.reconstruct_from_event(event)
```

## Testing
You need `pytest` installed in order to run the tests, see [pytest documentation](https://docs.pytest.org/en/stable/) for instructions.

The tests are located in `./python/test`.

To run them execute `pytest` in your console.

## linting, style and type hints
Linters used so far: pylint, pycodestyle, pydocstyle.

It's good practice to keep lines shorter than 80 characters, i.e. at most 79 characters per line.

Type hints can be verified using mypy (static type checker). It seems like there is currently no good way to include type hints of numpy types, however this will be adressed in the upcoming numpy version 1.20.

## The life of an event

### Generation
A path thorugh the dectector is randomly picked and represented by some data type (class).

input: Nothing

output: `ParticlePath`

### Simulation
The generated path is used to simulate what a real physical detector would output.

input: `ParticlePath`

output: `Event`

### Reconstruction
The Event data are used to reconstruct the underlying physical situation

input: `Event`

output: `ReconstructedPath`

### (Verification)
The results of the reconstruction step are verified against the initial physical assumption about what's happening inside the detector.

input: `ParticlePath`, `ReconstructedPath`

output: `Score`

### (Statistics)
A whole set of events in analysed.

input: Collection of `Score`s

output: Some kind of statistical analysis

## Program Architecture
Goals:
* Maintain good seperation between modules, facilitating parallel development.
* Reconstruction independent of data source. (should work with a real physical detector)

### Modules
* `generation`
* `simulation`
* `reconstruction`
* (`verification`)
* (`statistics`)
* (...)

### Common (core) types
* `EventId` (used for referrring to events)
* `DectectorGeometry` (geometric information about the detector)
* 

### (in-)dependencies
Just some notes about where boundaries might lie, what code should directly depend on what other code:

Main seperation is between `generation` + `simulation` and `reconstruction`.

Generation should not depend on detector geometry (?).

Generation should only be concerned with the physical system (e.g. collision, decay) at the heart of our detector.

Simulation and reconstruction both heavily rely on `DetectorGeometry` and some kind of physical theory (WIP, see below).

## Issues
A simpler architecture might be sufficient.

How do we plug in varying physical theories in order to verify them?

How do we store / transfer events between program steps?

## See also
<https://lhcb-comp.web.cern.ch/General/Publications/longpap-a152.pdf>
