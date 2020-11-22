# 23.11.2020 Meeting Protocol


## 1. Minutes from last meeting (10 min)

 * Does everybody have their SSH, key and GitLab account stuff sorted out?
 * Have we decided who takes ownership over each module? Or do a free-for all?
 * Igor: did you find references from coding style? will you share them?

## 2. Coordination Problems (5 min)

 * Sebastian and Nermine did not attend Saturday morning meeting.
 * What to do in the future?
 * What times are a definite no-go for everybody? (Shobith)


## 3. Agile Methods (20 min)

 * Think about last week's lecture notes and whether there is anything about the worflow we'd like to implement into our project.
 * Waterfall Method? We'd have the following checklist:
    * Requirements? Check.
    * Use cases? Save for testing?
    * Design Phase? Mostly done, thanks to Massin. Check. But is it worth making a flow-chart? Volunteers?
    * Implementation? Nope, lol. Still on it.
    * Verification? Nope, need to implement first. But note ```testing.py```
    * Maintenance? Probably not necessary for this project.
 * Scrum? Scrum!!!
    * Sprints would have to be about 1 to 2 weeks tops.
    * Define roles. Product owner: Igor / sMassin. Maybe split role? Scrum master. Sebastian, based on protocols
    * Do we want to change the meeting structure? i.e. go from one weekly "long" meeting to shorter ones 2-3 times a week? Discuss.
    * No daily Scrum due to project size / other responsibilities
    * Main lesson: Keep meeting time **fixed at 1 hour maximum** --> Meeting referee responsible for enforcing this
 * Estimating task durations, i.e. planning poker.
    * Do we want to do this or forego this altogether?


## 4. First Implementation, Massin (20 min)

 * Will give the floor to Massin to walk us through what he did.
 * Things to note:
    * ```get_radom_path``` can be immediately implemented from ```np.random.uniform```
    * Reconstructed paths should be stored somewhere, i.e. a DataFrame --> pandas
    * **Concern:** Defining everything in terms of classes/objects seem _too rigid_
      * all numerical stuffs could be done directly via functional programming.
    * no mention has been yet for which libraries should be used 

## 5. Sonstiges (5 min)

