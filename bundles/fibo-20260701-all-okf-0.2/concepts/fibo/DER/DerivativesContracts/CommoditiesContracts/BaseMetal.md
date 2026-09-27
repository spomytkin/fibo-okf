---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: base metal
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: common metal that tarnishes, oxidizes, or corrodes relatively quickly when exposed to air or moisture, that is
      widely used in commercial and industrial applications, such as construction and manufacturing
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Base metals or alloys include metals other than precious metals, such as copper, lead, zinc, tin, iron, steel,
      or brass. Note that iron and steel are included under metal and metal products in some classification schemes - see
      https://fred.stlouisfed.org/series/WPU101 for example.
  disjoint_with:
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount/PreciousMetal.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/PreciousMetal
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/CommoditiesContracts/Metal.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/CommoditiesContracts/Metal
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/CommoditiesContracts/BaseMetal
sources:
- id: fibo-source-e460829ab0
  resource: references/fibo/DER/DerivativesContracts/CommoditiesContracts.rdf
  sha256: e460829ab039670f9e06a5e2f7c8a0435a5c7529015e0dbe7a9a790464504bd8
  title: FIBO source DER/DerivativesContracts/CommoditiesContracts.rdf
title: base metal
type: Ontology Class
---

# base metal

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/CommoditiesContracts/BaseMetal>

## Definition

common metal that tarnishes, oxidizes, or corrodes relatively quickly when exposed to air or moisture, that is widely used in commercial and industrial applications, such as construction and manufacturing

## Relationships

- **Subclass of**: [Metal](/concepts/fibo/DER/DerivativesContracts/CommoditiesContracts/Metal.md)

## Constraints

- **Disjoint with**: [PreciousMetal](/concepts/fibo/FND/Accounting/CurrencyAmount/PreciousMetal.md)

## Annotations

- **label** (en): base metal
- **definition** (en): common metal that tarnishes, oxidizes, or corrodes relatively quickly when exposed to air or moisture, that is widely used in commercial and industrial applications, such as construction and manufacturing
- **explanatoryNote** (en): Base metals or alloys include metals other than precious metals, such as copper, lead, zinc, tin, iron, steel, or brass. Note that iron and steel are included under metal and metal products in some classification schemes - see https://fred.stlouisfed.org/series/WPU101 for example.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
