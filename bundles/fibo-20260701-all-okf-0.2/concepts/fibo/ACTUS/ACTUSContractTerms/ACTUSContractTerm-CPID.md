---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: ACTUS contract term - CPID
  - predicate: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/hasParameterName
    value: counterpartyID
  - predicate: https://www.omg.org/spec/Commons/Designators/hasDescription
    value: 'CPID identifies the counterparty to the CRID in this contract.


      CPID is ideally the official LEI which can be a firm, a government body, even a single person etc. However, this can
      also refer to a annonymous group in which case this information is not to be disclosed. CPID may also refer to a group
      taking a joint risk or more generally, CPID is the main counterparty, against which the contract has been settled.'
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTag
    value: CPID
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTextualName
    value: Counterparty Identifier
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm
  related_to:
  - concept: /concepts/fibo/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-Counterparty.md
    predicate: https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-Counterparty
resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm-CPID
sources:
- id: fibo-source-693c1adb8c
  resource: references/fibo/ACTUS/ACTUSContractTerms.rdf
  sha256: 693c1adb8cb72d5497fad9bf041c21f2b8c3852f8267b04a354a42a7ee38f986
  title: FIBO source ACTUS/ACTUSContractTerms.rdf
title: ACTUS contract term - CPID
type: Ontology Individual
---

# ACTUS contract term - CPID

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm-CPID>

## Relationships

- **Related to**: [ACTUSContractTermGroup-Counterparty](/concepts/fibo/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-Counterparty.md)

## Annotations

- **label**: ACTUS contract term - CPID
- **hasParameterName**: counterpartyID
- **hasDescription**: CPID identifies the counterparty to the CRID in this contract.  CPID is ideally the official LEI which can be a firm, a government body, even a single person etc. However, this can also refer to a annonymous group in which case this information is not to be disclosed. CPID may also refer to a group taking a joint risk or more generally, CPID is the main counterparty, against which the contract has been settled.
- **hasTag**: CPID
- **hasTextualName**: Counterparty Identifier

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
