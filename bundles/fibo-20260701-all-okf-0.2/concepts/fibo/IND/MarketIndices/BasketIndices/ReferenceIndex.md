---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: reference index
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: measure of change in the value of the contents of a basket over a given period of time
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: An index is a function based on a set of structured calculations with respect to a basket of credit risks, financial
      instruments or other indices over time. Analysis may be computed based on historical values, projected values, etc.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: benchmark
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/WeightedBasket
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/isBasedOn
  - cardinality: 1
    filler: https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDatePeriod
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Documents/hasReportingPeriod
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/RecurrenceInterval
    kind: all_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/hasPeriodicity
  - cardinality: 0
    filler: https://www.omg.org/spec/Commons/DatesAndTimes/Date
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/hasReleaseDate
  - cardinality: 0
    filler: https://www.omg.org/spec/Commons/DatesAndTimes/CombinedDateTime
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/hasReleaseDateTime
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/ClassificationSchemes/IndustrySectorClassifier
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesClassification/AssetClass
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy
  subclass_of:
  - concept: /concepts/fibo/FND/Utilities/Analytics/ScopedMeasure.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/ScopedMeasure
resource: https://spec.edmcouncil.org/fibo/ontology/IND/MarketIndices/BasketIndices/ReferenceIndex
sources:
- id: fibo-source-8b9b76e637
  resource: references/fibo/IND/MarketIndices/BasketIndices.rdf
  sha256: 8b9b76e637aa5b1332f4c7c5c8a862b34e591e273b3a9fd842a28ea66fc5c321
  title: FIBO source IND/MarketIndices/BasketIndices.rdf
title: reference index
type: Ontology Class
---

# reference index

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/MarketIndices/BasketIndices/ReferenceIndex>

## Definition

measure of change in the value of the contents of a basket over a given period of time

## Relationships

- **Subclass of**: [ScopedMeasure](/concepts/fibo/FND/Utilities/Analytics/ScopedMeasure.md)

## Constraints

- **[isBasedOn](/concepts/fibo/FBC/DebtAndEquities/Debt/isBasedOn.md)**: some values from of type [WeightedBasket](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/WeightedBasket.md)
- **[hasReportingPeriod](/concepts/fibo/FND/Arrangements/Documents/hasReportingPeriod.md)**: exact qualified cardinality 1 of type [ExplicitDatePeriod](<https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDatePeriod>)
- **[hasPeriodicity](/concepts/fibo/FND/Utilities/Analytics/hasPeriodicity.md)**: all values from of type [RecurrenceInterval](/concepts/fibo/FND/DatesAndTimes/FinancialDates/RecurrenceInterval.md)
- **[hasReleaseDate](/concepts/fibo/FND/Utilities/Analytics/hasReleaseDate.md)**: min qualified cardinality 0 of type [Date](<https://www.omg.org/spec/Commons/DatesAndTimes/Date>)
- **[hasReleaseDateTime](/concepts/fibo/FND/Utilities/Analytics/hasReleaseDateTime.md)**: min qualified cardinality 0 of type [CombinedDateTime](<https://www.omg.org/spec/Commons/DatesAndTimes/CombinedDateTime>)
- **[isClassifiedBy](<https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy>)**: min qualified cardinality 0 of type [IndustrySectorClassifier](/concepts/fibo/FND/Arrangements/ClassificationSchemes/IndustrySectorClassifier.md)
- **[isClassifiedBy](<https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy>)**: min qualified cardinality 0 of type [AssetClass](/concepts/fibo/SEC/Securities/SecuritiesClassification/AssetClass.md)

## Annotations

- **label** (en): reference index
- **definition** (en): measure of change in the value of the contents of a basket over a given period of time
- **explanatoryNote** (en): An index is a function based on a set of structured calculations with respect to a basket of credit risks, financial instruments or other indices over time. Analysis may be computed based on historical values, projected values, etc.
- **synonym** (en): benchmark

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
