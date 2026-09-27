---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: interest rate
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: amount charged, expressed as a percentage of principal, in exchange for the use of assets
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Interest rates are typically noted on an annual basis, known as the annual percentage rate (APR). The assets borrowed
      could include cash, consumer goods, and large assets such as a vehicle or building. The rate is derived by dividing
      the amount of interest by the amount of principal borrowed. Interest rates are quoted on bills, notes, bonds, credit
      cards, and many kinds of consumer and business loans.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: http://www.w3.org/2001/XMLSchema#decimal
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/hasRateValue
  subclass_of:
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount/PercentageMonetaryAmount.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/PercentageMonetaryAmount
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/InterestRate
sources:
- id: fibo-source-4355744519
  resource: references/fibo/FND/Accounting/CurrencyAmount.rdf
  sha256: 4355744519e448cbeeedd0e9601a43470dc1329a7cab73d807e7b99048db0032
  title: FIBO source FND/Accounting/CurrencyAmount.rdf
title: interest rate
type: Ontology Class
---

# interest rate

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/InterestRate>

## Definition

amount charged, expressed as a percentage of principal, in exchange for the use of assets

## Relationships

- **Subclass of**: [PercentageMonetaryAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/PercentageMonetaryAmount.md)

## Constraints

- **[hasRateValue](/concepts/fibo/FND/Accounting/CurrencyAmount/hasRateValue.md)**: exact qualified cardinality 1 of type [decimal](<http://www.w3.org/2001/XMLSchema#decimal>)

## Annotations

- **label**: interest rate
- **definition**: amount charged, expressed as a percentage of principal, in exchange for the use of assets
- **explanatoryNote**: Interest rates are typically noted on an annual basis, known as the annual percentage rate (APR). The assets borrowed could include cash, consumer goods, and large assets such as a vehicle or building. The rate is derived by dividing the amount of interest by the amount of principal borrowed. Interest rates are quoted on bills, notes, bonds, credit cards, and many kinds of consumer and business loans.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
