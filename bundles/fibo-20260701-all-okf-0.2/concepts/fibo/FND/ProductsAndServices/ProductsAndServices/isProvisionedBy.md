---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: is provisioned by
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: identifies the service provider that provisions the service or facility
  inverse_of:
  - concept: /concepts/fibo/FND/ProductsAndServices/ProductsAndServices/provisions.md
    predicate: http://www.w3.org/2002/07/owl#inverseOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/provisions
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://www.omg.org/spec/Commons/Organizations/ServiceProvider
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/Organizations/isProvidedBy
resource: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/isProvisionedBy
sources:
- id: fibo-source-7f330c2b6d
  resource: references/fibo/FND/ProductsAndServices/ProductsAndServices.rdf
  sha256: 7f330c2b6de4e90f2c5d728ddf32af1d75f320646040450c1da9a8c5f8740548
  title: FIBO source FND/ProductsAndServices/ProductsAndServices.rdf
title: is provisioned by
type: Ontology Property
---

# is provisioned by

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/isProvisionedBy>

## Definition

identifies the service provider that provisions the service or facility

## Relationships

- **Inverse of**: [provisions](/concepts/fibo/FND/ProductsAndServices/ProductsAndServices/provisions.md)
- **Range**: [ServiceProvider](<https://www.omg.org/spec/Commons/Organizations/ServiceProvider>)
- **Subproperty of**: [isProvidedBy](<https://www.omg.org/spec/Commons/Organizations/isProvidedBy>)

## Annotations

- **label**: is provisioned by
- **definition**: identifies the service provider that provisions the service or facility

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
