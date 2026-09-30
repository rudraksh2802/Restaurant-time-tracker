# Requirements

## Functional Requirements

**FR1 - Occupancy:** record the number of people inside.

**FR2 - Queue:** record the number of groups waiting outside.

**FR3 - Available Seats:** calculate capacity minus occupancy.

**FR4 - Waiting Time:** estimate wait using queue size and average table turnover.

**FR5 - Customer Calculator:** add travel time and estimated wait.

**FR6 - Storage:** save and load current data using JSON.

**FR7 - Validation:** reject invalid values such as negative occupancy or occupancy above capacity.

## Nonfunctional Requirements

**NFR1 - Usability:** simple menu and readable output.

**NFR2 - Reliability:** invalid input should show an error instead of crashing the program.

**NFR3 - Maintainability:** separate files for main logic, storage and testing.

**NFR4 - Performance:** calculations should complete immediately for normal inputs.

**NFR5 - Resource Efficiency:** use lightweight local storage and Python standard library features.

**NFR6 - Scalability:** structure should allow future camera input, databases and multiple restaurants.
