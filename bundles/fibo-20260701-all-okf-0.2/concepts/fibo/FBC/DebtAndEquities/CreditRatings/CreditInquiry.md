---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: credit inquiry
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: request from a lender to a credit repository to obtain information regarding a prospective borrower's creditworthiness
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://www.omg.org/spec/Commons/PartiesAndSituations/Party
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditRatings/concernsParty
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditRatings/CreditRatingAgency
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Reporting/isRequestedOf
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditRatings/CreditInquiryType
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy
  subclass_of:
  - concept: /concepts/fibo/FND/Arrangements/Reporting/RequestActivity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Reporting/RequestActivity
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditRatings/CreditInquiry
sources:
- id: fibo-source-1f582cd28a
  resource: references/fibo/FBC/DebtAndEquities/CreditRatings.rdf
  sha256: 1f582cd28aa6fc7dddfffeabef7c4aed9e4a1274b09047548096bd1769f759b7
  title: FIBO source FBC/DebtAndEquities/CreditRatings.rdf
title: credit inquiry
type: Ontology Class
---

# credit inquiry

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditRatings/CreditInquiry>

## Definition

request from a lender to a credit repository to obtain information regarding a prospective borrower's creditworthiness

## Relationships

- **Subclass of**: [RequestActivity](/concepts/fibo/FND/Arrangements/Reporting/RequestActivity.md)

## Constraints

- **[concernsParty](/concepts/fibo/FBC/DebtAndEquities/CreditRatings/concernsParty.md)**: some values from of type [Party](<https://www.omg.org/spec/Commons/PartiesAndSituations/Party>)
- **[isRequestedOf](/concepts/fibo/FND/Arrangements/Reporting/isRequestedOf.md)**: some values from of type [CreditRatingAgency](/concepts/fibo/FBC/DebtAndEquities/CreditRatings/CreditRatingAgency.md)
- **[isClassifiedBy](<https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy>)**: some values from of type [CreditInquiryType](/concepts/fibo/FBC/DebtAndEquities/CreditRatings/CreditInquiryType.md)

## Annotations

- **label**: credit inquiry
- **definition**: request from a lender to a credit repository to obtain information regarding a prospective borrower's creditworthiness

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
