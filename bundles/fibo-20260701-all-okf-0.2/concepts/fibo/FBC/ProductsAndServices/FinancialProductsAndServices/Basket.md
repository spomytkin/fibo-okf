---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: basket
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: collection of goods, services, or other things (e.g., financial contracts) that can be purchased and sold in some
      marketplace
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A basket may be associated with a specific market sector, and may be delineated for the purposes of statistical
      analysis, such as for calculating CPI. According to the US Bureau of Labor Statistics (BLS), with respect to the CPI,
      a market basket is a package of goods and services that consumers purchase for day-to-day living. The weight of each
      item is based on the amount of expenditure reported by a sample of households.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: From a securities perspective, a basket is a collection of products or securities that are designated to mimic
      the performance of a market. For investors, the market basket is the principal idea behind index funds, which are essentially
      a broad sample of stocks, bonds or other securities in the market; this provides investors with a benchmark against
      which to compare their investment returns.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://www.omg.org/spec/Commons/PartiesAndSituations/Party
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/hasSelectingParty
  - cardinality: 0
    filler: http://www.w3.org/2001/XMLSchema#string
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/hasSelectionCriteria
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/BasketConstituent
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/hasMember
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Collections/Collection
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/Basket
sources:
- id: fibo-source-4fc675338a
  resource: references/fibo/FBC/ProductsAndServices/FinancialProductsAndServices.rdf
  sha256: 4fc675338a28c5419555e56e545b4aa6b0686d14777b4b852624b166d585b5ca
  title: FIBO source FBC/ProductsAndServices/FinancialProductsAndServices.rdf
title: basket
type: Ontology Class
---

# basket

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/Basket>

## Definition

collection of goods, services, or other things (e.g., financial contracts) that can be purchased and sold in some marketplace

## Relationships

- **Subclass of**: [Collection](<https://www.omg.org/spec/Commons/Collections/Collection>)

## Constraints

- **[hasSelectingParty](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/hasSelectingParty.md)**: min qualified cardinality 0 of type [Party](<https://www.omg.org/spec/Commons/PartiesAndSituations/Party>)
- **[hasSelectionCriteria](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/hasSelectionCriteria.md)**: min qualified cardinality 0 of type [string](<http://www.w3.org/2001/XMLSchema#string>)
- **[hasMember](<https://www.omg.org/spec/Commons/Collections/hasMember>)**: some values from of type [BasketConstituent](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/BasketConstituent.md)

## Annotations

- **label**: basket
- **definition**: collection of goods, services, or other things (e.g., financial contracts) that can be purchased and sold in some marketplace
- **explanatoryNote**: A basket may be associated with a specific market sector, and may be delineated for the purposes of statistical analysis, such as for calculating CPI. According to the US Bureau of Labor Statistics (BLS), with respect to the CPI, a market basket is a package of goods and services that consumers purchase for day-to-day living. The weight of each item is based on the amount of expenditure reported by a sample of households.
- **explanatoryNote**: From a securities perspective, a basket is a collection of products or securities that are designated to mimic the performance of a market. For investors, the market basket is the principal idea behind index funds, which are essentially a broad sample of stocks, bonds or other securities in the market; this provides investors with a benchmark against which to compare their investment returns.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
