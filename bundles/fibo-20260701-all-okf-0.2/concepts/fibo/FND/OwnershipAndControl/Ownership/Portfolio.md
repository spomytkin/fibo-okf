---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: portfolio
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: collection of holdings assembled and maintained as a unit for management purposes to achieve strategic objectives
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: http://www.investopedia.com/terms/h/holdings.asp
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: http://www.investopedia.com/terms/p/portfolio.asp
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: "The holdings of any given portfolio may include a variety of investment products, including stocks, bonds and\
      \ mutual funds to options, futures and exchange-traded funds, and relatively esoteric instruments such as private equity\
      \ and hedge funds as well as other assets of the owner, such as interests in real estate, art, or vehicles. \n\nWith\
      \ respect to financial assets, the number and nature of holdings contribute to the degree of diversification of a portfolio.\
      \ A mix of stocks across different sectors, bonds of different maturities, and other investments would suggest a well-diversified\
      \ portfolio, while concentrated holdings in a handful of stocks within a single sector indicates a portfolio with limited\
      \ diversification."
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: all_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/isHeldBy
    value: N3e2f5c3158c14d20b7e0c6f0ebe39ff4
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/Holding
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/comprises
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/Portfolio
    kind: max_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Collections/isMemberOf
  - kind: some_values_from
    property: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    value: N3844ac9036984ff5b100272672738b98
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Collections/Collection
resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/Portfolio
sources:
- id: fibo-source-4fc675338a
  resource: references/fibo/FBC/ProductsAndServices/FinancialProductsAndServices.rdf
  sha256: 4fc675338a28c5419555e56e545b4aa6b0686d14777b4b852624b166d585b5ca
  title: FIBO source FBC/ProductsAndServices/FinancialProductsAndServices.rdf
- id: fibo-source-de57f166a6
  resource: references/fibo/FND/OwnershipAndControl/Ownership.rdf
  sha256: de57f166a681de4546904cb9a49d26917586e61cebb91ca017cc3bda8df3a305
  title: FIBO source FND/OwnershipAndControl/Ownership.rdf
title: portfolio
type: Ontology Class
---

# portfolio

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/Portfolio>

## Definition

collection of holdings assembled and maintained as a unit for management purposes to achieve strategic objectives

## Relationships

- **Subclass of**: [Collection](<https://www.omg.org/spec/Commons/Collections/Collection>)

## Constraints

- **[isHeldBy](/concepts/fibo/FND/Relations/Relations/isHeldBy.md)**: all values from value `N3e2f5c3158c14d20b7e0c6f0ebe39ff4`
- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: some values from of type [Holding](/concepts/fibo/FND/OwnershipAndControl/Ownership/Holding.md)
- **[isMemberOf](<https://www.omg.org/spec/Commons/Collections/isMemberOf>)**: max qualified cardinality 1 of type [Portfolio](/concepts/fibo/FND/OwnershipAndControl/Ownership/Portfolio.md)
- **[isManagedBy](<https://www.omg.org/spec/Commons/Organizations/isManagedBy>)**: some values from value `N3844ac9036984ff5b100272672738b98`

## Annotations

- **label**: portfolio
- **definition**: collection of holdings assembled and maintained as a unit for management purposes to achieve strategic objectives
- **adaptedFrom**: http://www.investopedia.com/terms/h/holdings.asp
- **adaptedFrom**: http://www.investopedia.com/terms/p/portfolio.asp
- **explanatoryNote**: The holdings of any given portfolio may include a variety of investment products, including stocks, bonds and mutual funds to options, futures and exchange-traded funds, and relatively esoteric instruments such as private equity and hedge funds as well as other assets of the owner, such as interests in real estate, art, or vehicles.   With respect to financial assets, the number and nature of holdings contribute to the degree of diversification of a portfolio. A mix of stocks across different sectors, bonds of different maturities, and other investments would suggest a well-diversified portfolio, while concentrated holdings in a handful of stocks within a single sector indicates a portfolio with limited diversification.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
