---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: buyer
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: party that purchases something in exchange for money or other consideration under a contract of sale
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A buyer is the party that acquires, or agrees to acquire, ownership (in case of goods), or benefit or usage (in
      case of rights or services), something in the context of a sale, and may or may not be an end user of the product, good,
      service, or right.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: buyer
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: purchaser
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/Product
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/buys
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/PartyRole
resource: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/Buyer
sources:
- id: fibo-source-7f330c2b6d
  resource: references/fibo/FND/ProductsAndServices/ProductsAndServices.rdf
  sha256: 7f330c2b6de4e90f2c5d728ddf32af1d75f320646040450c1da9a8c5f8740548
  title: FIBO source FND/ProductsAndServices/ProductsAndServices.rdf
title: buyer
type: Ontology Class
---

# buyer

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/Buyer>

## Definition

party that purchases something in exchange for money or other consideration under a contract of sale

## Relationships

- **Subclass of**: [PartyRole](<https://www.omg.org/spec/Commons/PartiesAndSituations/PartyRole>)

## Constraints

- **[buys](/concepts/fibo/FND/ProductsAndServices/ProductsAndServices/buys.md)**: some values from of type [Product](/concepts/fibo/FND/ProductsAndServices/ProductsAndServices/Product.md)

## Annotations

- **label**: buyer
- **definition**: party that purchases something in exchange for money or other consideration under a contract of sale
- **explanatoryNote**: A buyer is the party that acquires, or agrees to acquire, ownership (in case of goods), or benefit or usage (in case of rights or services), something in the context of a sale, and may or may not be an end user of the product, good, service, or right.
- **synonym**: buyer
- **synonym**: purchaser

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
