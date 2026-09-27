---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: green bond
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: bond issued specifically to fund climate or environmental projects
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: These bonds are typically asset-linked and backed by the issuer's balance sheet. Green bonds finance projects aimed
      at energy efficiency, pollution prevention, sustainable agriculture, fishery and forestry, the protection of aquatic
      and terrestrial ecosystems, clean transportation, sustainable water management and the cultivation of environmentally
      friendly technologies, and often include incentives such as tax exemption.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/Bonds/Bond.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/Bond
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/GreenBond
sources:
- id: fibo-source-e8d406159e
  resource: references/fibo/SEC/Debt/Bonds.rdf
  sha256: e8d406159e34a92dc8e87cfce162f6fc67e075db2b2f73c520d41f7419bb0844
  title: FIBO source SEC/Debt/Bonds.rdf
title: green bond
type: Ontology Class
---

# green bond

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/GreenBond>

## Definition

bond issued specifically to fund climate or environmental projects

## Relationships

- **Subclass of**: [Bond](/concepts/fibo/SEC/Debt/Bonds/Bond.md)

## Annotations

- **label**: green bond
- **definition**: bond issued specifically to fund climate or environmental projects
- **explanatoryNote**: These bonds are typically asset-linked and backed by the issuer's balance sheet. Green bonds finance projects aimed at energy efficiency, pollution prevention, sustainable agriculture, fishery and forestry, the protection of aquatic and terrestrial ecosystems, clean transportation, sustainable water management and the cultivation of environmentally friendly technologies, and often include incentives such as tax exemption.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
