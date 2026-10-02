---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: agency mortgage pool creation process
  disjoint_with:
  - concept: /concepts/fibo/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/NonAgencyPoolCreationProcess.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/NonAgencyPoolCreationProcess
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://www.omg.org/spec/Commons/DatesAndTimes/Date
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/DatesAndTimes/hasEndDate
  - filler: https://www.omg.org/spec/Commons/DatesAndTimes/Date
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/DatesAndTimes/hasStartDate
  - filler: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/AgencyMBSIssuance/PassThroughMBSSecuritizationProcess
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/DatesAndTimes/precedes
  subclass_of:
  - concept: /concepts/fibo/BP/SecuritiesIssuance/DebtIssuance/RetailAssetPoolCreationProcess.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/DebtIssuance/RetailAssetPoolCreationProcess
resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/AgencyMBSIssuance/AgencyMortgagePoolCreationProcess
sources:
- id: fibo-source-2eeca2019d
  resource: references/fibo/BP/SecuritiesIssuance/AgencyMBSIssuance.rdf
  sha256: 2eeca2019d428c47ac1513eaf8db629142182da83295878f53a62e84592f6a59
  title: FIBO source BP/SecuritiesIssuance/AgencyMBSIssuance.rdf
title: agency mortgage pool creation process
type: Ontology Class
---

# agency mortgage pool creation process

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/AgencyMBSIssuance/AgencyMortgagePoolCreationProcess>

## Relationships

- **Subclass of**: [RetailAssetPoolCreationProcess](/concepts/fibo/BP/SecuritiesIssuance/DebtIssuance/RetailAssetPoolCreationProcess.md)

## Constraints

- **Disjoint with**: [NonAgencyPoolCreationProcess](/concepts/fibo/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/NonAgencyPoolCreationProcess.md)
- **[hasEndDate](<https://www.omg.org/spec/Commons/DatesAndTimes/hasEndDate>)**: some values from of type [Date](<https://www.omg.org/spec/Commons/DatesAndTimes/Date>)
- **[hasStartDate](<https://www.omg.org/spec/Commons/DatesAndTimes/hasStartDate>)**: some values from of type [Date](<https://www.omg.org/spec/Commons/DatesAndTimes/Date>)
- **[precedes](<https://www.omg.org/spec/Commons/DatesAndTimes/precedes>)**: some values from of type [PassThroughMBSSecuritizationProcess](/concepts/fibo/BP/SecuritiesIssuance/AgencyMBSIssuance/PassThroughMBSSecuritizationProcess.md)

## Annotations

- **label** (en): agency mortgage pool creation process

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
