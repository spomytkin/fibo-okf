---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: capital-labor-energy-materials multifactor productivity
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: ratio of a quantity index of gross output to a quantity index of combined inputs
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: KLEMS-MFP
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: http://www.oecd.org/std/productivity-stats/2352458.pdf
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Shows the time profile of how productively combined inputs are used to generate gross output. Conceptually, the
      KLEMS productivity measure captures disembodied technical change. In practice, it reflects also efficiency change, economies
      of scale, variations in capacity utilisation and measurement errors.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: KLEMS multifactor productivity
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/IND/EconomicIndicators/EconomicIndicators/Productivity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/Productivity
resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/CapitalLaborEnergyMaterialsMultifactorProductivity
sources:
- id: fibo-source-8403bfa401
  resource: references/fibo/IND/EconomicIndicators/EconomicIndicators.rdf
  sha256: 8403bfa40177c207d84c314ab9dc8e157b1928c8ac8b2d5ba84d9260106576c5
  title: FIBO source IND/EconomicIndicators/EconomicIndicators.rdf
title: capital-labor-energy-materials multifactor productivity
type: Ontology Class
---

# capital-labor-energy-materials multifactor productivity

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/CapitalLaborEnergyMaterialsMultifactorProductivity>

## Definition

ratio of a quantity index of gross output to a quantity index of combined inputs

## Relationships

- **Subclass of**: [Productivity](/concepts/fibo/IND/EconomicIndicators/EconomicIndicators/Productivity.md)

## Annotations

- **label**: capital-labor-energy-materials multifactor productivity
- **definition**: ratio of a quantity index of gross output to a quantity index of combined inputs
- **abbreviation**: KLEMS-MFP
- **adaptedFrom**: http://www.oecd.org/std/productivity-stats/2352458.pdf
- **explanatoryNote**: Shows the time profile of how productively combined inputs are used to generate gross output. Conceptually, the KLEMS productivity measure captures disembodied technical change. In practice, it reflects also efficiency change, economies of scale, variations in capacity utilisation and measurement errors.
- **synonym**: KLEMS multifactor productivity

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
