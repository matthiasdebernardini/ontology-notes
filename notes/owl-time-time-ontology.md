# OWL-Time (Time Ontology)

**What it is**

OWL-Time is an OWL 2 DL ontology for describing temporal properties of resources. It covers ordering relations among instants and intervals, durations, and temporal positions expressed in Gregorian date-time or other temporal reference systems such as Unix time, geologic time, and alternative calendars.

**Key concepts**
- `time:TemporalEntity` has the two subclasses `time:Interval` and `time:Instant`; beginning, end, duration, and generic time-association properties connect temporal descriptions to entities.
- Allen-style interval relations—such as before, meets, overlaps, during, starts, and finishes—support qualitative ordering and relative-position reasoning.
- `time:TRS`, `time:TimePosition`, `time:GeneralDateTimeDescription`, and `time:TemporalUnit` support coordinate, ordinal, and calendar-clock representations with explicit reference systems and precision.

**How you'd use it**

Attach an instant, interval, or duration to an event or other resource, then represent its position with an XSD date-time, a structured date-time description, or a value in a named temporal reference system. Use the interval relations when relative ordering matters more than a single timestamp.

**LLM angle**

none stated

**Pitfalls & lessons**

The fetched document is a Candidate Recommendation Draft and says it should be cited as work in progress. Calendar arithmetic is not uniformly exact: Gregorian months have variable length, leap-second handling differs from ISO 8601, detailed time-zone definitions are outside the ontology, temporal vagueness is not addressed explicitly, and time series are out of scope.

**Verdict**

A broad, reusable temporal vocabulary when data must combine instants, intervals, durations, and non-Gregorian or ordinal reference systems; its stated scope boundaries and draft status should be accounted for.

## Sources consulted
- https://www.w3.org/TR/owl-time/
- `sources/owl-time-time-ontology.txt`
