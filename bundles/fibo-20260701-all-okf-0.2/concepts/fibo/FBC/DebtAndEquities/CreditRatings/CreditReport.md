---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: credit report
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: report describing the creditworthiness and related credit attributes of a borrower
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: This is typically provided by a credit rating agency but could be produced by an internal proprietary model as
      well.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://www.omg.org/spec/Commons/PartiesAndSituations/Party
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditRatings/concernsParty
  - filler: https://www.omg.org/spec/Commons/DatesAndTimes/DatePeriod
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditRatings/hasCoveragePeriod
  - filler: https://www.omg.org/spec/Commons/DatesAndTimes/Date
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/hasAsOfDate
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditRatings/CreditReportProduct
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/exemplifies
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditRatings/CreditRatingAgency
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/isProducedBy
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditRatings/CreditReportCategory
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditRatings/CreditInquiry
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Collections/comprises
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditRatings/CreditMessage
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Collections/comprises
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditRatings/CreditRating
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Collections/comprises
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditRatings/CreditTradeline
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Collections/comprises
  - cardinality: 0
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Documents/hasDataSource
  - cardinality: 0
    filler: https://www.omg.org/spec/Commons/Identifiers/Identifier
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Identifiers/isIdentifiedBy
  subclass_of:
  - concept: /concepts/fibo/FND/Arrangements/Ratings/RatingReport.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Ratings/RatingReport
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditRatings/CreditReport
sources:
- id: fibo-source-1f582cd28a
  resource: references/fibo/FBC/DebtAndEquities/CreditRatings.rdf
  sha256: 1f582cd28aa6fc7dddfffeabef7c4aed9e4a1274b09047548096bd1769f759b7
  title: FIBO source FBC/DebtAndEquities/CreditRatings.rdf
title: credit report
type: Ontology Class
---

# credit report

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditRatings/CreditReport>

## Definition

report describing the creditworthiness and related credit attributes of a borrower

## Relationships

- **Subclass of**: [RatingReport](/concepts/fibo/FND/Arrangements/Ratings/RatingReport.md)

## Constraints

- **[concernsParty](/concepts/fibo/FBC/DebtAndEquities/CreditRatings/concernsParty.md)**: some values from of type [Party](<https://www.omg.org/spec/Commons/PartiesAndSituations/Party>)
- **[hasCoveragePeriod](/concepts/fibo/FBC/DebtAndEquities/CreditRatings/hasCoveragePeriod.md)**: some values from of type [DatePeriod](<https://www.omg.org/spec/Commons/DatesAndTimes/DatePeriod>)
- **[hasAsOfDate](/concepts/fibo/FND/DatesAndTimes/FinancialDates/hasAsOfDate.md)**: some values from of type [Date](<https://www.omg.org/spec/Commons/DatesAndTimes/Date>)
- **[exemplifies](/concepts/fibo/FND/Relations/Relations/exemplifies.md)**: min qualified cardinality 0 of type [CreditReportProduct](/concepts/fibo/FBC/DebtAndEquities/CreditRatings/CreditReportProduct.md)
- **[isProducedBy](/concepts/fibo/FND/Relations/Relations/isProducedBy.md)**: min qualified cardinality 0 of type [CreditRatingAgency](/concepts/fibo/FBC/DebtAndEquities/CreditRatings/CreditRatingAgency.md)
- **[isClassifiedBy](<https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy>)**: min qualified cardinality 0 of type [CreditReportCategory](/concepts/fibo/FBC/DebtAndEquities/CreditRatings/CreditReportCategory.md)
- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: min qualified cardinality 0 of type [CreditInquiry](/concepts/fibo/FBC/DebtAndEquities/CreditRatings/CreditInquiry.md)
- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: min qualified cardinality 0 of type [CreditMessage](/concepts/fibo/FBC/DebtAndEquities/CreditRatings/CreditMessage.md)
- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: min qualified cardinality 0 of type [CreditRating](/concepts/fibo/FBC/DebtAndEquities/CreditRatings/CreditRating.md)
- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: min qualified cardinality 0 of type [CreditTradeline](/concepts/fibo/FBC/DebtAndEquities/CreditRatings/CreditTradeline.md)
- **[hasDataSource](<https://www.omg.org/spec/Commons/Documents/hasDataSource>)**: min qualified cardinality 0
- **[isIdentifiedBy](<https://www.omg.org/spec/Commons/Identifiers/isIdentifiedBy>)**: min qualified cardinality 0 of type [Identifier](<https://www.omg.org/spec/Commons/Identifiers/Identifier>)

## Annotations

- **label**: credit report
- **definition**: report describing the creditworthiness and related credit attributes of a borrower
- **explanatoryNote**: This is typically provided by a credit rating agency but could be produced by an internal proprietary model as well.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
