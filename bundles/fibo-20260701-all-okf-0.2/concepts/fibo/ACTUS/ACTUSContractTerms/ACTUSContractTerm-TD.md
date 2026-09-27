---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: ACTUS contract term - TD
  - predicate: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/hasParameterMapping
    value: Starting from the contract, fibo-fnd-arr-doc:hasTerminationDate cmns-dt:Date; cmns-dt:hasDateValue xsd:string
  - predicate: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/hasParameterName
    value: terminationDate
  - predicate: https://www.omg.org/spec/Commons/Designators/hasDescription
    value: 'If a contract is sold before MD (for example a bond on the secondary market) this date has to be set. It refers
      to the date at which the payment (of PTD) and transfer of the security happens. In other words, TD - if set - takes
      the role otherwise MD has from a cash flow perspective.


      Note, CPID of the CT is not the counterparty of the transaction.'
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTag
    value: TD
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTextualName
    value: Termination Date
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm
  related_to:
  - concept: /concepts/fibo/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-NotionalPrincipal.md
    predicate: https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-NotionalPrincipal
resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm-TD
sources:
- id: fibo-source-1ffe76217e
  resource: references/fibo/ACTUS/ACTUSContractTermMapping.rdf
  sha256: 1ffe76217e0123653c8a4d03290dcfab352af9fe7a5cdb369ae0e86c55d11bbd
  title: FIBO source ACTUS/ACTUSContractTermMapping.rdf
- id: fibo-source-693c1adb8c
  resource: references/fibo/ACTUS/ACTUSContractTerms.rdf
  sha256: 693c1adb8cb72d5497fad9bf041c21f2b8c3852f8267b04a354a42a7ee38f986
  title: FIBO source ACTUS/ACTUSContractTerms.rdf
title: ACTUS contract term - TD
type: Ontology Individual
---

# ACTUS contract term - TD

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm-TD>

## Relationships

- **Related to**: [ACTUSContractTermGroup-NotionalPrincipal](/concepts/fibo/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-NotionalPrincipal.md)

## Annotations

- **label**: ACTUS contract term - TD
- **hasParameterMapping**: Starting from the contract, fibo-fnd-arr-doc:hasTerminationDate cmns-dt:Date; cmns-dt:hasDateValue xsd:string
- **hasParameterName**: terminationDate
- **hasDescription**: If a contract is sold before MD (for example a bond on the secondary market) this date has to be set. It refers to the date at which the payment (of PTD) and transfer of the security happens. In other words, TD - if set - takes the role otherwise MD has from a cash flow perspective.  Note, CPID of the CT is not the counterparty of the transaction.
- **hasTag**: TD
- **hasTextualName**: Termination Date

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
