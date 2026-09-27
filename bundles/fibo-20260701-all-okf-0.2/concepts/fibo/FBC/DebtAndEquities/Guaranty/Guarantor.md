---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: guarantor
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: party that guarantees, endorses, or provides indemnity for some obligation on behalf of some other party
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: Barron's Dictionary of Business and Economics Terms, Fifth Edition, 2012
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: In some cases, the party acting as guarantor may also be a party to the contract, such as in the case of Fannie
      Mae or Freddie Mac. In such cases, the same individual would be modeled as having both roles.
  defined_by:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Guaranty.md
    predicate: http://www.w3.org/2000/01/rdf-schema#isDefinedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Guaranty/
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://www.omg.org/spec/Commons/Organizations/LegalPerson
    kind: all_values_from
    property: https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy
  - kind: some_values_from
    property: https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy
    value: N1a84ba70e2f4450c8dab484e89bcb075
  subclass_of:
  - concept: /concepts/fibo/BE/OwnershipAndControl/ControlParties/DeJureControllingInterestParty.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/ControlParties/DeJureControllingInterestParty
  - concept: /concepts/fibo/FND/Agreements/Contracts/ContractThirdParty.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/ContractThirdParty
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Guaranty/Guarantor
sources:
- id: fibo-source-a6bc9592ee
  resource: references/fibo/FBC/DebtAndEquities/Guaranty.rdf
  sha256: a6bc9592eeebb061e99b2dc168751d4b3612dbcc32c86c50959e17011e4247b0
  title: FIBO source FBC/DebtAndEquities/Guaranty.rdf
title: guarantor
type: Ontology Class
---

# guarantor

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Guaranty/Guarantor>

## Definition

party that guarantees, endorses, or provides indemnity for some obligation on behalf of some other party

## Relationships

- **Defined by**: [Guaranty](/concepts/fibo/FBC/DebtAndEquities/Guaranty.md)
- **Subclass of**: [DeJureControllingInterestParty](/concepts/fibo/BE/OwnershipAndControl/ControlParties/DeJureControllingInterestParty.md)
- **Subclass of**: [ContractThirdParty](/concepts/fibo/FND/Agreements/Contracts/ContractThirdParty.md)

## Constraints

- **[isPlayedBy](<https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy>)**: all values from of type [LegalPerson](<https://www.omg.org/spec/Commons/Organizations/LegalPerson>)
- **[isPlayedBy](<https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy>)**: some values from value `N1a84ba70e2f4450c8dab484e89bcb075`

## Annotations

- **label**: guarantor
- **definition**: party that guarantees, endorses, or provides indemnity for some obligation on behalf of some other party
- **adaptedFrom**: Barron's Dictionary of Business and Economics Terms, Fifth Edition, 2012
- **explanatoryNote**: In some cases, the party acting as guarantor may also be a party to the contract, such as in the case of Fannie Mae or Freddie Mac. In such cases, the same individual would be modeled as having both roles.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
