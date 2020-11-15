# ParticlePixelDetector

## The life of an event

### Generation
A path thorugh the dectector is randomly picked and represented by some data type (class).

input: Nothing

output: `PhysicalPath`

### Simulation
The generated path is used to simulate what a real physical detector would output.

input: `PhysicalPath`

output: `Event`

### Reconstruction
The Event data are used to reconstruct the underlying physical situation

input: `Event`

output: `ReconstructedPath`

<span style="color:grey">

### (Verification)
The results of the reconstruction step are verified against the initial physical assumption about what's happening inside the detector.

input: `PhysicalPath`, `ReconstructedPath`

output: `Score`

### (Statistics)
A whole set of events in analysed.

input: Collection of `Score`s

output: Some kind of statistical analysis

</span>

## Program Architecture
Goals:
* Maintain good seperation between modules, facilitating parallel development.
* Reconstruction independent of data source. (should work with a real physical detector)

### Modules
* `generation`
* `simulation`
* `reconstruction`

<span style="color:grey">

* (`verification`)
* (`statistics`)
* (...)

</span>

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

## Issues so far
How do we plug in varying physical theories in order to verify them?

How do we store / transfer events between program steps?
