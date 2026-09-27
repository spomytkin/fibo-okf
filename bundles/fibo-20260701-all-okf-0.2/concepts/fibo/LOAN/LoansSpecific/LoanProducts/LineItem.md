---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: line item
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: description of a product or service including its unit cost, number of units and total cost
  - predicate: http://www.w3.org/2004/02/skos/core#editorialNote
    value: 'Future consideration: move this to ProductsAndServices ontology (fibo-fnd-pas-pas).'
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/MonetaryAmount
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/hasCost
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/MonetaryAmount
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/LoanProducts/hasUnitCost
  - kind: some_values_from
    property: https://www.omg.org/spec/Commons/Documents/refersTo
    value: N6e0e191b1711401c95accaf1057d3a44
  - cardinality: 0
    filler: http://www.w3.org/2001/XMLSchema#decimal
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasNumericValue
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Collections/Constituent
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/LoanProducts/LineItem
sources:
- id: fibo-source-1b62e30b1c
  resource: references/fibo/LOAN/LoansSpecific/LoanProducts.rdf
  sha256: 1b62e30b1c3693cc85e718679f9b231242d1342cdfc54a4c99663db4f26a8644
  title: FIBO source LOAN/LoansSpecific/LoanProducts.rdf
title: line item
type: Ontology Class
---

# line item

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/LoanProducts/LineItem>

## Definition

description of a product or service including its unit cost, number of units and total cost

## Relationships

- **Subclass of**: [Constituent](<https://www.omg.org/spec/Commons/Collections/Constituent>)

## Constraints

- **[hasCost](/concepts/fibo/LOAN/LoansGeneral/Loans/hasCost.md)**: some values from of type [MonetaryAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryAmount.md)
- **[hasUnitCost](/concepts/fibo/LOAN/LoansSpecific/LoanProducts/hasUnitCost.md)**: min qualified cardinality 0 of type [MonetaryAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryAmount.md)
- **[refersTo](<https://www.omg.org/spec/Commons/Documents/refersTo>)**: some values from value `N6e0e191b1711401c95accaf1057d3a44`
- **[hasNumericValue](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasNumericValue>)**: min qualified cardinality 0 of type [decimal](<http://www.w3.org/2001/XMLSchema#decimal>)

## Annotations

- **label**: line item
- **definition**: description of a product or service including its unit cost, number of units and total cost
- **editorialNote**: Future consideration: move this to ProductsAndServices ontology (fibo-fnd-pas-pas).

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
