---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: new housing sector
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: a classifier for a sector of the economy used for price indices focused on contractors' selling prices of new residential
      houses, where detailed specifications pertaining to each house remain the same between two consecutive periods
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: http://www23.statcan.gc.ca/imdb/p2SV.pl?Function=getSurvey&SDDS=2310
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FND/Arrangements/ClassificationSchemes/IndustrySectorClassifier.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/ClassificationSchemes/IndustrySectorClassifier
resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/NorthAmericanIndicators/CAEconomicIndicators/NewHousingSector
sources:
- id: fibo-source-a06a0301d8
  resource: references/fibo/IND/EconomicIndicators/NorthAmericanIndicators/CAEconomicIndicators.rdf
  sha256: a06a0301d8cf8f8081904fa368ef17074ae7806ea3c96fa34eb61634f9bc05d6
  title: FIBO source IND/EconomicIndicators/NorthAmericanIndicators/CAEconomicIndicators.rdf
title: new housing sector
type: Ontology Class
---

# new housing sector

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/NorthAmericanIndicators/CAEconomicIndicators/NewHousingSector>

## Definition

a classifier for a sector of the economy used for price indices focused on contractors' selling prices of new residential houses, where detailed specifications pertaining to each house remain the same between two consecutive periods

## Relationships

- **Subclass of**: [IndustrySectorClassifier](/concepts/fibo/FND/Arrangements/ClassificationSchemes/IndustrySectorClassifier.md)

## Annotations

- **label**: new housing sector
- **definition**: a classifier for a sector of the economy used for price indices focused on contractors' selling prices of new residential houses, where detailed specifications pertaining to each house remain the same between two consecutive periods
- **adaptedFrom**: http://www23.statcan.gc.ca/imdb/p2SV.pl?Function=getSurvey&SDDS=2310

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
