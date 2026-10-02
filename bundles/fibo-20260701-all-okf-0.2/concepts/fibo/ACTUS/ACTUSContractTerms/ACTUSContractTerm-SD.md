---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: ACTUS contract term - SD
  - predicate: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/hasParameterMapping
    value: Starting from the contract, fibo-fnd-dt-oc:hasEventDate cmns-dt:Date; cmns-dt:hasDateValue xsd:string
  - predicate: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/hasParameterName
    value: statusDate
  - predicate: https://www.omg.org/spec/Commons/Designators/hasDescription
    value: SD holds the date per which all attributes of the record were updated. This is especially important for the highly
      dynamic attributes like Accruals, Notional, interest rates in variable instruments etc.
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTag
    value: SD
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTextualName
    value: Status Date
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm
  related_to:
  - concept: /concepts/fibo/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-ContractIdentification.md
    predicate: https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-ContractIdentification
resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm-SD
sources:
- id: fibo-source-1ffe76217e
  resource: references/fibo/ACTUS/ACTUSContractTermMapping.rdf
  sha256: 1ffe76217e0123653c8a4d03290dcfab352af9fe7a5cdb369ae0e86c55d11bbd
  title: FIBO source ACTUS/ACTUSContractTermMapping.rdf
- id: fibo-source-693c1adb8c
  resource: references/fibo/ACTUS/ACTUSContractTerms.rdf
  sha256: 693c1adb8cb72d5497fad9bf041c21f2b8c3852f8267b04a354a42a7ee38f986
  title: FIBO source ACTUS/ACTUSContractTerms.rdf
title: ACTUS contract term - SD
type: Ontology Individual
---

# ACTUS contract term - SD

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm-SD>

## Relationships

- **Related to**: [ACTUSContractTermGroup-ContractIdentification](/concepts/fibo/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-ContractIdentification.md)

## Annotations

- **label**: ACTUS contract term - SD
- **hasParameterMapping**: Starting from the contract, fibo-fnd-dt-oc:hasEventDate cmns-dt:Date; cmns-dt:hasDateValue xsd:string
- **hasParameterName**: statusDate
- **hasDescription**: SD holds the date per which all attributes of the record were updated. This is especially important for the highly dynamic attributes like Accruals, Notional, interest rates in variable instruments etc.
- **hasTag**: SD
- **hasTextualName**: Status Date

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
