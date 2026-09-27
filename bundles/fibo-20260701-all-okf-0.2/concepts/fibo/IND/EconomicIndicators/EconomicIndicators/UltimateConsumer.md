---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: ultimate consumer
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: person that is the ultimate user of a good, product or service
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: For the purposes of the CPI and related statistics, the definition of consumer is limited to humans. In general,
      a consumer could include a pet, as the consumer of pet food, for example, although the pet owner would likely be the
      purchaser and target of advertising.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The consumer is not always the purchaser of the product. Consumers are considered to be the users of the final
      product. For example, purchasers of building products are interim users of these products while constructing the finished
      product, which then may be purchased by the consumer.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: consumer as defined by the Consumer Price Index (CPI)
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/Person
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy
  subclass_of:
  - concept: /concepts/fibo/FND/ProductsAndServices/ProductsAndServices/Consumer.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/Consumer
resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/UltimateConsumer
sources:
- id: fibo-source-8403bfa401
  resource: references/fibo/IND/EconomicIndicators/EconomicIndicators.rdf
  sha256: 8403bfa40177c207d84c314ab9dc8e157b1928c8ac8b2d5ba84d9260106576c5
  title: FIBO source IND/EconomicIndicators/EconomicIndicators.rdf
title: ultimate consumer
type: Ontology Class
---

# ultimate consumer

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/UltimateConsumer>

## Definition

person that is the ultimate user of a good, product or service

## Relationships

- **Subclass of**: [Consumer](/concepts/fibo/FND/ProductsAndServices/ProductsAndServices/Consumer.md)

## Constraints

- **[isPlayedBy](<https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy>)**: some values from of type [Person](/concepts/fibo/FND/AgentsAndPeople/People/Person.md)

## Annotations

- **label**: ultimate consumer
- **definition**: person that is the ultimate user of a good, product or service
- **explanatoryNote**: For the purposes of the CPI and related statistics, the definition of consumer is limited to humans. In general, a consumer could include a pet, as the consumer of pet food, for example, although the pet owner would likely be the purchaser and target of advertising.
- **explanatoryNote**: The consumer is not always the purchaser of the product. Consumers are considered to be the users of the final product. For example, purchasers of building products are interim users of these products while constructing the finished product, which then may be purchased by the consumer.
- **synonym**: consumer as defined by the Consumer Price Index (CPI)

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
