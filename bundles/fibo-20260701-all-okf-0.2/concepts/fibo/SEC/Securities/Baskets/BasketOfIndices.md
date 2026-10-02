---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: market basket
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: basket composed of market indices
  - predicate: http://www.w3.org/2004/02/skos/core#example
    value: For example, certain equities derivatives have an underlying basket which is a basket of more than one index, not
      a basket of securities.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/Baskets/BasketOfIndicesConstituent
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/hasMember
  subclass_of:
  - concept: /concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/WeightedBasket.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/WeightedBasket
  - concept: /concepts/fibo/FND/DatesAndTimes/FinancialDates/DatedStructuredCollection.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/DatedStructuredCollection
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/Baskets/BasketOfIndices
sources:
- id: fibo-source-f1997b0934
  resource: references/fibo/SEC/Securities/Baskets.rdf
  sha256: f1997b0934adf3676bd3123e6e96393a1aca9f7d83555f75bfd2dd84b1723bcf
  title: FIBO source SEC/Securities/Baskets.rdf
title: market basket
type: Ontology Class
---

# market basket

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/Baskets/BasketOfIndices>

## Definition

basket composed of market indices

## Relationships

- **Subclass of**: [WeightedBasket](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/WeightedBasket.md)
- **Subclass of**: [DatedStructuredCollection](/concepts/fibo/FND/DatesAndTimes/FinancialDates/DatedStructuredCollection.md)

## Constraints

- **[hasMember](<https://www.omg.org/spec/Commons/Collections/hasMember>)**: some values from of type [BasketOfIndicesConstituent](/concepts/fibo/SEC/Securities/Baskets/BasketOfIndicesConstituent.md)

## Annotations

- **label**: market basket
- **definition**: basket composed of market indices
- **example**: For example, certain equities derivatives have an underlying basket which is a basket of more than one index, not a basket of securities.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
