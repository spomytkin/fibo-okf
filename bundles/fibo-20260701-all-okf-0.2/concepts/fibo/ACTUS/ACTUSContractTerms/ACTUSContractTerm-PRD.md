---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: ACTUS contract term - PRD
  - predicate: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/hasParameterMapping
    value: Starting from the contract, fibo-fnd-dt-fd:hasAcquisitionDate cmns-dt:CombinedDateTime
  - predicate: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/hasParameterName
    value: purchaseDate
  - predicate: https://www.omg.org/spec/Commons/Designators/hasDescription
    value: 'If a contract is bought after initiation (for example a bond on the secondary market) this date has to be set.
      It refers to the date at which the payment (of PPRD) and transfer of the security happens. In other words, PRD - if
      set - takes the role otherwise IED has from a cash flow perspective.


      Note, CPID of the CT is not the counterparty of the transaction.'
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTag
    value: PRD
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTextualName
    value: Purchase Date
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm
  related_to:
  - concept: /concepts/fibo/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-NotionalPrincipal.md
    predicate: https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-NotionalPrincipal
resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm-PRD
sources:
- id: fibo-source-1ffe76217e
  resource: references/fibo/ACTUS/ACTUSContractTermMapping.rdf
  sha256: 1ffe76217e0123653c8a4d03290dcfab352af9fe7a5cdb369ae0e86c55d11bbd
  title: FIBO source ACTUS/ACTUSContractTermMapping.rdf
- id: fibo-source-693c1adb8c
  resource: references/fibo/ACTUS/ACTUSContractTerms.rdf
  sha256: 693c1adb8cb72d5497fad9bf041c21f2b8c3852f8267b04a354a42a7ee38f986
  title: FIBO source ACTUS/ACTUSContractTerms.rdf
title: ACTUS contract term - PRD
type: Ontology Individual
---

# ACTUS contract term - PRD

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm-PRD>

## Relationships

- **Related to**: [ACTUSContractTermGroup-NotionalPrincipal](/concepts/fibo/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-NotionalPrincipal.md)

## Annotations

- **label**: ACTUS contract term - PRD
- **hasParameterMapping**: Starting from the contract, fibo-fnd-dt-fd:hasAcquisitionDate cmns-dt:CombinedDateTime
- **hasParameterName**: purchaseDate
- **hasDescription**: If a contract is bought after initiation (for example a bond on the secondary market) this date has to be set. It refers to the date at which the payment (of PPRD) and transfer of the security happens. In other words, PRD - if set - takes the role otherwise IED has from a cash flow perspective.  Note, CPID of the CT is not the counterparty of the transaction.
- **hasTag**: PRD
- **hasTextualName**: Purchase Date

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
