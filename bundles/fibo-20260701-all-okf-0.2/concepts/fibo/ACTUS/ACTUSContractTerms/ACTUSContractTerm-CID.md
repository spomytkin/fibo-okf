---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: ACTUS contract term - CID
  - predicate: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/hasParameterMapping
    value: Starting from the contract, cmns-id:isIdentifiedBy cmns-id:Identifier; cmns-txt;hasTextValue xsd:string
  - predicate: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/hasParameterName
    value: contractID
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/usageNote
    value: Financial instrument identifier is the range of the property cmns-id;isIdentifiedBy in the case of any financial
      instrument, including most loans. In order to map this to ACTUS data, the property, 'is identified by' should be used
      together with the identifier, where the identifier for the contract may be a CUSIP, SEDOL code, FIGI, or something else,
      including a bespoke identifier for a contract traded over the counter, non-tradable contract such as many credit agreements,
      and the like. Typically, CID would denote a financial instrument identifier.
  - predicate: https://www.omg.org/spec/Commons/Designators/hasDescription
    value: 'Unique identifier of a contract.


      If the system is used on a single firm level, an internal unique ID can be generated. If used on a national or globally
      level, a globally unique ID is required.'
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTag
    value: CID
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTextualName
    value: Contract Identifier
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm
  related_to:
  - concept: /concepts/fibo/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-ContractIdentification.md
    predicate: https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-ContractIdentification
resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm-CID
sources:
- id: fibo-source-1ffe76217e
  resource: references/fibo/ACTUS/ACTUSContractTermMapping.rdf
  sha256: 1ffe76217e0123653c8a4d03290dcfab352af9fe7a5cdb369ae0e86c55d11bbd
  title: FIBO source ACTUS/ACTUSContractTermMapping.rdf
- id: fibo-source-693c1adb8c
  resource: references/fibo/ACTUS/ACTUSContractTerms.rdf
  sha256: 693c1adb8cb72d5497fad9bf041c21f2b8c3852f8267b04a354a42a7ee38f986
  title: FIBO source ACTUS/ACTUSContractTerms.rdf
title: ACTUS contract term - CID
type: Ontology Individual
---

# ACTUS contract term - CID

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm-CID>

## Relationships

- **Related to**: [ACTUSContractTermGroup-ContractIdentification](/concepts/fibo/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-ContractIdentification.md)

## Annotations

- **label**: ACTUS contract term - CID
- **hasParameterMapping**: Starting from the contract, cmns-id:isIdentifiedBy cmns-id:Identifier; cmns-txt;hasTextValue xsd:string
- **hasParameterName**: contractID
- **usageNote**: Financial instrument identifier is the range of the property cmns-id;isIdentifiedBy in the case of any financial instrument, including most loans. In order to map this to ACTUS data, the property, 'is identified by' should be used together with the identifier, where the identifier for the contract may be a CUSIP, SEDOL code, FIGI, or something else, including a bespoke identifier for a contract traded over the counter, non-tradable contract such as many credit agreements, and the like. Typically, CID would denote a financial instrument identifier.
- **hasDescription**: Unique identifier of a contract.  If the system is used on a single firm level, an internal unique ID can be generated. If used on a national or globally level, a globally unique ID is required.
- **hasTag**: CID
- **hasTextualName**: Contract Identifier

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
