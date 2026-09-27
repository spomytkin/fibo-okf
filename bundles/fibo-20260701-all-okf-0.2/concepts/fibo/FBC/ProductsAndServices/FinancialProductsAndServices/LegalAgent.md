---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: legal agent
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: any party that has been legally empowered to act on behalf of another party
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: 17 CFR 45.1, Definitions - see the definition of agent
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: some_values_from
    property: https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy
    value: Nfb77d79d956c47d3926fb93291fe71f8
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/AgentRole
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/LegalAgent
sources:
- id: fibo-source-4fc675338a
  resource: references/fibo/FBC/ProductsAndServices/FinancialProductsAndServices.rdf
  sha256: 4fc675338a28c5419555e56e545b4aa6b0686d14777b4b852624b166d585b5ca
  title: FIBO source FBC/ProductsAndServices/FinancialProductsAndServices.rdf
title: legal agent
type: Ontology Class
---

# legal agent

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/LegalAgent>

## Definition

any party that has been legally empowered to act on behalf of another party

## Relationships

- **Subclass of**: [AgentRole](<https://www.omg.org/spec/Commons/PartiesAndSituations/AgentRole>)

## Constraints

- **[isPlayedBy](<https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy>)**: some values from value `Nfb77d79d956c47d3926fb93291fe71f8`

## Annotations

- **label**: legal agent
- **definition**: any party that has been legally empowered to act on behalf of another party
- **adaptedFrom**: 17 CFR 45.1, Definitions - see the definition of agent

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
