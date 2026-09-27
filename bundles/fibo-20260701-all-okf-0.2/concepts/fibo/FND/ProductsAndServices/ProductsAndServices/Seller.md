---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: seller
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: party that makes, offers or contracts to make a sale to an actual or potential buyer
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: purveyor
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: vendor
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/Product
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/sells
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/PartyRole
resource: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/Seller
sources:
- id: fibo-source-7f330c2b6d
  resource: references/fibo/FND/ProductsAndServices/ProductsAndServices.rdf
  sha256: 7f330c2b6de4e90f2c5d728ddf32af1d75f320646040450c1da9a8c5f8740548
  title: FIBO source FND/ProductsAndServices/ProductsAndServices.rdf
title: seller
type: Ontology Class
---

# seller

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/Seller>

## Definition

party that makes, offers or contracts to make a sale to an actual or potential buyer

## Relationships

- **Subclass of**: [PartyRole](<https://www.omg.org/spec/Commons/PartiesAndSituations/PartyRole>)

## Constraints

- **[sells](/concepts/fibo/FND/ProductsAndServices/ProductsAndServices/sells.md)**: some values from of type [Product](/concepts/fibo/FND/ProductsAndServices/ProductsAndServices/Product.md)

## Annotations

- **label**: seller
- **definition**: party that makes, offers or contracts to make a sale to an actual or potential buyer
- **synonym**: purveyor
- **synonym**: vendor

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
