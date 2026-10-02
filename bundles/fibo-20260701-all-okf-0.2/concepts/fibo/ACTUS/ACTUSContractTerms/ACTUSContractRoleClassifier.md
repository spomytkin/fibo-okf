---
owl:
  annotations:
  - predicate: http://purl.org/dc/terms/description
    value: "CNTRL defines which position the CRID (the identifier for the creator of the data about the contract, i.e., the\
      \ record for the contract, which currently must be a contract party, not a third party, such as a regulator, but not\
      \ necessarily the originator) takes in a contract. For example, whether the contract is an asset or liability, a long\
      \ or short position for the CRID. Note that this may change as ACTUS evolves beyond the current known implementations\
      \ and libraries for processing the contract.\n\nMost contracts are simple on or off balance sheet positions which are\
      \ assets, liabilities. Such contracts can also play a secondary role as a collateral. \n\nThe attribute is highly significant\
      \ since it determines the direction of all cash flows. The exact meaning is given with each CT in the ACTUS High Level\
      \ Specification document."
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: ACTUS contract role classifier
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: classifier for various roles that are relevant to how the contract is processed by a particular contract party
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: CNTRL
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: Contract Role
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: contractRole
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://www.omg.org/spec/Commons/RolesAndCompositions/Role
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Classifiers/classifies
  - kind: has_value
    property: https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy
    value: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-ContractIdentification
  - filler: https://www.omg.org/spec/Commons/RolesAndCompositions/Role
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Designators/denotes
  subclass_of:
  - concept: /concepts/fibo/ACTUS/ACTUSContractTerms/ACTUSContractTerm.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Classifiers/Classifier
resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractRoleClassifier
sources:
- id: fibo-source-693c1adb8c
  resource: references/fibo/ACTUS/ACTUSContractTerms.rdf
  sha256: 693c1adb8cb72d5497fad9bf041c21f2b8c3852f8267b04a354a42a7ee38f986
  title: FIBO source ACTUS/ACTUSContractTerms.rdf
title: ACTUS contract role classifier
type: Ontology Class
---

# ACTUS contract role classifier

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractRoleClassifier>

## Definition

classifier for various roles that are relevant to how the contract is processed by a particular contract party

## Relationships

- **Subclass of**: [ACTUSContractTerm](/concepts/fibo/ACTUS/ACTUSContractTerms/ACTUSContractTerm.md)
- **Subclass of**: [Classifier](<https://www.omg.org/spec/Commons/Classifiers/Classifier>)

## Constraints

- **[classifies](<https://www.omg.org/spec/Commons/Classifiers/classifies>)**: some values from of type [Role](<https://www.omg.org/spec/Commons/RolesAndCompositions/Role>)
- **[isClassifiedBy](<https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy>)**: has value value `https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-ContractIdentification`
- **[denotes](<https://www.omg.org/spec/Commons/Designators/denotes>)**: some values from of type [Role](<https://www.omg.org/spec/Commons/RolesAndCompositions/Role>)

## Annotations

- **description**: CNTRL defines which position the CRID (the identifier for the creator of the data about the contract, i.e., the record for the contract, which currently must be a contract party, not a third party, such as a regulator, but not necessarily the originator) takes in a contract. For example, whether the contract is an asset or liability, a long or short position for the CRID. Note that this may change as ACTUS evolves beyond the current known implementations and libraries for processing the contract.  Most contracts are simple on or off balance sheet positions which are assets, liabilities. Such contracts can also play a secondary role as a collateral.   The attribute is highly significant since it determines the direction of all cash flows. The exact meaning is given with each CT in the ACTUS High Level Specification document.
- **label**: ACTUS contract role classifier
- **definition**: classifier for various roles that are relevant to how the contract is processed by a particular contract party
- **abbreviation**: CNTRL
- **synonym**: Contract Role
- **synonym**: contractRole

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
