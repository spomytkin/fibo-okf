---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: basket Of indices constituent
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: single constituent of a basket of indices
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDate
    kind: max_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/hasDateAdded
  - kind: all_values_from
    property: https://www.omg.org/spec/Commons/Collections/comprises
    value: N8a53826cdd10401886bc367f5191ded9
  subclass_of:
  - concept: /concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/WeightedBasketConstituent.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/WeightedBasketConstituent
  - concept: /concepts/fibo/FND/DatesAndTimes/FinancialDates/DatedCollectionConstituent.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/DatedCollectionConstituent
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/Baskets/BasketOfIndicesConstituent
sources:
- id: fibo-source-f1997b0934
  resource: references/fibo/SEC/Securities/Baskets.rdf
  sha256: f1997b0934adf3676bd3123e6e96393a1aca9f7d83555f75bfd2dd84b1723bcf
  title: FIBO source SEC/Securities/Baskets.rdf
title: basket Of indices constituent
type: Ontology Class
---

# basket Of indices constituent

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/Baskets/BasketOfIndicesConstituent>

## Definition

single constituent of a basket of indices

## Relationships

- **Subclass of**: [WeightedBasketConstituent](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/WeightedBasketConstituent.md)
- **Subclass of**: [DatedCollectionConstituent](/concepts/fibo/FND/DatesAndTimes/FinancialDates/DatedCollectionConstituent.md)

## Constraints

- **[hasDateAdded](/concepts/fibo/FND/DatesAndTimes/FinancialDates/hasDateAdded.md)**: max qualified cardinality 1 of type [ExplicitDate](<https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDate>)
- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: all values from value `N8a53826cdd10401886bc367f5191ded9`

## Annotations

- **label**: basket Of indices constituent
- **definition**: single constituent of a basket of indices

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
