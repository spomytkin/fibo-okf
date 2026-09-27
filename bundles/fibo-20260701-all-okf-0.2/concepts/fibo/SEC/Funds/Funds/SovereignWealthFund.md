---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: sovereign wealth fund
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: state-owned investment fund that consists of pools of money derived from a country's reserves
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Sovereign wealth funds include the International Monetary Fund, whose corresponding legal entity is a polity.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: social wealth fund
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: sovereign investment fund
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/SEC/Securities/Pools/CollectiveInvestmentVehicle.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/Pools/CollectiveInvestmentVehicle
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/Funds/SovereignWealthFund
sources:
- id: fibo-source-a82c11f42e
  resource: references/fibo/SEC/Funds/Funds.rdf
  sha256: a82c11f42ef79a0f83aeae8434ad054ddef746da9d97126ef3d8923eacf9c275
  title: FIBO source SEC/Funds/Funds.rdf
title: sovereign wealth fund
type: Ontology Class
---

# sovereign wealth fund

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/Funds/SovereignWealthFund>

## Definition

state-owned investment fund that consists of pools of money derived from a country's reserves

## Relationships

- **Subclass of**: [CollectiveInvestmentVehicle](/concepts/fibo/SEC/Securities/Pools/CollectiveInvestmentVehicle.md)

## Annotations

- **label** (en): sovereign wealth fund
- **definition** (en): state-owned investment fund that consists of pools of money derived from a country's reserves
- **explanatoryNote** (en): Sovereign wealth funds include the International Monetary Fund, whose corresponding legal entity is a polity.
- **synonym** (en): social wealth fund
- **synonym** (en): sovereign investment fund

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
