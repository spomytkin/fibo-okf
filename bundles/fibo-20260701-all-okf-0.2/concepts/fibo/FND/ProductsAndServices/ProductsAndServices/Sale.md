---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: sale
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: exchange of goods or services for money
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/MonetaryAmount
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/hasPrice
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/Buyer
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/hasBuyer
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/Seller
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/hasSeller
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/Product
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo
  subclass_of:
  - concept: /concepts/fibo/FND/ProductsAndServices/ProductsAndServices/TransactionEvent.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/TransactionEvent
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/Situation
resource: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/Sale
sources:
- id: fibo-source-7f330c2b6d
  resource: references/fibo/FND/ProductsAndServices/ProductsAndServices.rdf
  sha256: 7f330c2b6de4e90f2c5d728ddf32af1d75f320646040450c1da9a8c5f8740548
  title: FIBO source FND/ProductsAndServices/ProductsAndServices.rdf
title: sale
type: Ontology Class
---

# sale

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/Sale>

## Definition

exchange of goods or services for money

## Relationships

- **Subclass of**: [TransactionEvent](/concepts/fibo/FND/ProductsAndServices/ProductsAndServices/TransactionEvent.md)
- **Subclass of**: [Situation](<https://www.omg.org/spec/Commons/PartiesAndSituations/Situation>)

## Constraints

- **[hasPrice](/concepts/fibo/FND/Accounting/CurrencyAmount/hasPrice.md)**: some values from of type [MonetaryAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryAmount.md)
- **[hasBuyer](/concepts/fibo/FND/ProductsAndServices/ProductsAndServices/hasBuyer.md)**: some values from of type [Buyer](/concepts/fibo/FND/ProductsAndServices/ProductsAndServices/Buyer.md)
- **[hasSeller](/concepts/fibo/FND/ProductsAndServices/ProductsAndServices/hasSeller.md)**: some values from of type [Seller](/concepts/fibo/FND/ProductsAndServices/ProductsAndServices/Seller.md)
- **[appliesTo](<https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo>)**: some values from of type [Product](/concepts/fibo/FND/ProductsAndServices/ProductsAndServices/Product.md)

## Annotations

- **label**: sale
- **definition**: exchange of goods or services for money

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
