---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: ACTUS contract term - CRID
  - predicate: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/hasParameterMapping
    value: Starting from the contract principal, originator, or issuer, cmns-rlcmp:isPlayedBy cmns-pts:Party; cmns-id:isIdentifiedBy
      cmns-id:Identifier; cmns-txt;hasTextValue xsd:string
  - predicate: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/hasParameterName
    value: creatorID
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: This is called the creator identifier in the ACTUS applicability rules.
  - predicate: https://www.omg.org/spec/Commons/Designators/hasDescription
    value: 'This identifies the legal entity creating the contract record. The counterparty of the contract is tracked in
      CPID.


      CRID is ideally the official LEI which can be a firm, a government body, even a single person etc. However, this can
      also refer to a annonymous group in which case this information is not to be disclosed. CRID may also refer to a group
      taking a joint risk.'
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTag
    value: CRID
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTextualName
    value: Creator Identifier
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm
  related_to:
  - concept: /concepts/fibo/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-ContractIdentification.md
    predicate: https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-ContractIdentification
resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm-CRID
sources:
- id: fibo-source-1ffe76217e
  resource: references/fibo/ACTUS/ACTUSContractTermMapping.rdf
  sha256: 1ffe76217e0123653c8a4d03290dcfab352af9fe7a5cdb369ae0e86c55d11bbd
  title: FIBO source ACTUS/ACTUSContractTermMapping.rdf
- id: fibo-source-693c1adb8c
  resource: references/fibo/ACTUS/ACTUSContractTerms.rdf
  sha256: 693c1adb8cb72d5497fad9bf041c21f2b8c3852f8267b04a354a42a7ee38f986
  title: FIBO source ACTUS/ACTUSContractTerms.rdf
title: ACTUS contract term - CRID
type: Ontology Individual
---

# ACTUS contract term - CRID

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm-CRID>

## Relationships

- **Related to**: [ACTUSContractTermGroup-ContractIdentification](/concepts/fibo/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-ContractIdentification.md)

## Annotations

- **label**: ACTUS contract term - CRID
- **hasParameterMapping**: Starting from the contract principal, originator, or issuer, cmns-rlcmp:isPlayedBy cmns-pts:Party; cmns-id:isIdentifiedBy cmns-id:Identifier; cmns-txt;hasTextValue xsd:string
- **hasParameterName**: creatorID
- **explanatoryNote**: This is called the creator identifier in the ACTUS applicability rules.
- **hasDescription**: This identifies the legal entity creating the contract record. The counterparty of the contract is tracked in CPID.  CRID is ideally the official LEI which can be a firm, a government body, even a single person etc. However, this can also refer to a annonymous group in which case this information is not to be disclosed. CRID may also refer to a group taking a joint risk.
- **hasTag**: CRID
- **hasTextualName**: Creator Identifier

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
