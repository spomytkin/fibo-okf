---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: letter of credit
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: letter from a bank or other creditworthy institution guaranteeing that a buyer's payment to a seller will be received
      on time and for the correct amount
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: L/C
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: In some states in the U.S., the issuer is not limited to financial institutions -- it is simply a written instrument,
      addressed by one person to another, requesting the latter to give credit to the person in whose favor it is drawn.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: In the event that the buyer is unable to make payment, the bank or other issuer is required to cover the full or
      remaining amount.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://www.omg.org/spec/Commons/PartiesAndSituations/PartyRole
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/isIssuedBy
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/FinancialAsset
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/RolesAndCompositions/playsRole
  subclass_of:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Debt/CommittedCreditFacility.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/CommittedCreditFacility
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Guaranty/LetterOfCredit
sources:
- id: fibo-source-a6bc9592ee
  resource: references/fibo/FBC/DebtAndEquities/Guaranty.rdf
  sha256: a6bc9592eeebb061e99b2dc168751d4b3612dbcc32c86c50959e17011e4247b0
  title: FIBO source FBC/DebtAndEquities/Guaranty.rdf
title: letter of credit
type: Ontology Class
---

# letter of credit

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Guaranty/LetterOfCredit>

## Definition

letter from a bank or other creditworthy institution guaranteeing that a buyer's payment to a seller will be received on time and for the correct amount

## Relationships

- **Subclass of**: [CommittedCreditFacility](/concepts/fibo/FBC/DebtAndEquities/Debt/CommittedCreditFacility.md)

## Constraints

- **[isIssuedBy](/concepts/fibo/FND/Relations/Relations/isIssuedBy.md)**: some values from of type [PartyRole](<https://www.omg.org/spec/Commons/PartiesAndSituations/PartyRole>)
- **[playsRole](<https://www.omg.org/spec/Commons/RolesAndCompositions/playsRole>)**: some values from of type [FinancialAsset](/concepts/fibo/FND/OwnershipAndControl/Ownership/FinancialAsset.md)

## Annotations

- **label**: letter of credit
- **definition**: letter from a bank or other creditworthy institution guaranteeing that a buyer's payment to a seller will be received on time and for the correct amount
- **abbreviation**: L/C
- **explanatoryNote**: In some states in the U.S., the issuer is not limited to financial institutions -- it is simply a written instrument, addressed by one person to another, requesting the latter to give credit to the person in whose favor it is drawn.
- **explanatoryNote**: In the event that the buyer is unable to make payment, the bank or other issuer is required to cover the full or remaining amount.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
