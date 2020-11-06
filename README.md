# octree completion

For reasons that aren't important right now, here is thing.

Let's say you are doing a project that can be subdivided into tasks/areas.

The cells are independent of each other, and you're interested in measuring progress.

Here is an example of how that can be done and how it can be formatted.

An example would be a hotel where all rooms are to be renovated. You don't care about specifically when a specific room is done, you just want to make sure that *all* rooms are done, and really you want to make sure all *floors* are done.

And let's say they only have to be painted. Then the completion of the floors depends on the completion of the rooms. And you don't really care to see the rooms if you don't have to. I.e. You want to see at a glance of the floor table if there are rooms that are still do be done or not. Then if there are floors still to be done, you want there to be a detailed table to see which room is blocking progress for the floor.

Ignore the ugly.

"Floor" cells table:

|Unnamed: 0|1|2|3|Unnamed: 4|
|--- |--- |--- |--- |--- |
|0|0.888889|0.888889|1.000000|NaN|
|1|0.777778|0.777778|0.833333|NaN|
|2|0.944444|0.944444|0.777778|NaN|

"Room" cells table:

|Unnamed: 0|00|01|02|10|11|12|20|21|22|Unnamed: 10|
|--- |--- |--- |--- |--- |--- |--- |--- |--- |--- |--- |
|0|0.5|1|1.0|1.0|0.5|1.0|1.0|1.0|1.0|NaN|
|1|1.0|1|0.5|0.5|0.5|0.5|1.0|1.0|1.0|NaN|
|2|1.0|1|1.0|1.0|1.0|1.0|1.0|1.0|0.5|NaN|
|10|0.5|1|1.0|0.5|1.0|0.5|1.0|1.0|0.5|NaN|
|11|0.5|1|1.0|0.5|1.0|1.0|1.0|1.0|1.0|NaN|
|12|1.0|1|1.0|1.0|0.5|1.0|1.0|1.0|1.0|NaN|
|20|1.0|1|1.0|1.0|0.5|1.0|1.0|0.5|0.5|NaN|
|21|1.0|1|1.0|1.0|1.0|0.5|0.5|1.0|1.0|NaN|
|22|1.0|1|1.0|1.0|1.0|0.5|0.5|1.0|1.0|NaN|





