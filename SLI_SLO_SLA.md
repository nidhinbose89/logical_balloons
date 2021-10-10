Developers try to be agile, while Operators strive for stability/security.

SRE
- Define availability
- Level of availability
- Plan in case of failure

Define metrics in advance and agree on it.
100% availability is not realistic.

Understand and agree what availability means in the context of the service under design/development.
Need to have quantifiable numerical indicators to define availability.

SLI
Inform about the direct health of the system.
- Request latency
- Batch throughput
- Failures per N requests
These are aggregated over time.

Samples:
- 95th percentile latency of homepage requests over past 5 minutes < 300ms.
- Is the 99th percentile latency of requests received in the past 5 mins, less than 300ms?
- Is ratio of errors to total requests received in past 5 minutes less than 1%?

Note - 
A percentile (or a centile) is a measure used in statistics indicating 
the value below which a given percentage of observations in a group of 
observations fall. The term 95th percentile refers to the point at which
5% of a population set will exceed the referenced value. 

SLO
- Agreed upon bounds on how often SLIs must be met!
- Binding targets for a collection of SLIs -- Its an accumulation/integration of SLI over time.
- Has upper and lower bounds.
- Samples
- 95th percentile homepage SLI will succeed 99.9% over trailing year.
- is the total downtime/delay over year > x hours as previously agreed or less than y hours.
  

SLA
This is what I am going to do, if I dont meet the expected reliability -- a promise.
Business agreement between a customer and service provider based on SLO.
Remedial steps/Ramifications required if service is out of spec according to contract will be put in.
Sample:
- Service credits if 95th percentile homepage SLI succeeds less than 99.5% over trailing year.

SLA is more lenient than SLO. SLAs is build on top of SLOs.
SLAs drives SLOs which inform SLAs

SRE works with SLOs.
