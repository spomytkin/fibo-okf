---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: pass through m b s securitization process
  disjoint_with:
  - concept: /concepts/fibo/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/TranchedMBSSecuritizationProcess.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/TranchedMBSSecuritizationProcess
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://www.omg.org/spec/Commons/DatesAndTimes/Date
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/DatesAndTimes/hasEndDate
  - filler: https://www.omg.org/spec/Commons/DatesAndTimes/Date
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/DatesAndTimes/hasStartDate
  subclass_of:
  - concept: /concepts/fibo/BP/SecuritiesIssuance/MBSIssuance/MBSSecuritizationProcess.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MBSIssuance/MBSSecuritizationProcess
resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/AgencyMBSIssuance/PassThroughMBSSecuritizationProcess
sources:
- id: fibo-source-2eeca2019d
  resource: references/fibo/BP/SecuritiesIssuance/AgencyMBSIssuance.rdf
  sha256: 2eeca2019d428c47ac1513eaf8db629142182da83295878f53a62e84592f6a59
  title: FIBO source BP/SecuritiesIssuance/AgencyMBSIssuance.rdf
title: pass through m b s securitization process
type: Ontology Class
---

# pass through m b s securitization process

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/AgencyMBSIssuance/PassThroughMBSSecuritizationProcess>

## Relationships

- **Subclass of**: [MBSSecuritizationProcess](/concepts/fibo/BP/SecuritiesIssuance/MBSIssuance/MBSSecuritizationProcess.md)

## Constraints

- **Disjoint with**: [TranchedMBSSecuritizationProcess](/concepts/fibo/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/TranchedMBSSecuritizationProcess.md)
- **[hasEndDate](<https://www.omg.org/spec/Commons/DatesAndTimes/hasEndDate>)**: some values from of type [Date](<https://www.omg.org/spec/Commons/DatesAndTimes/Date>)
- **[hasStartDate](<https://www.omg.org/spec/Commons/DatesAndTimes/hasStartDate>)**: some values from of type [Date](<https://www.omg.org/spec/Commons/DatesAndTimes/Date>)

## Annotations

- **label** (en): pass through m b s securitization process

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
