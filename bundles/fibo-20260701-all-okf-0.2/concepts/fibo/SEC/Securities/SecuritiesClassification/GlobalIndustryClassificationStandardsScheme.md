---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Global Industry Classification Standards scheme
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: classification scheme that is a hierarchical four-level system classifying companies based on the principal business
      activity of the organization
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/acronym
    value: GICS
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.msci.com/our-solutions/indexes/gics
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: 'The four tiers are: Sectors, Industry Groups, Industries and Sub-Industries. All definitions are standardized
      and applied to companies globally. Each company is assigned a single GICS classification in each of the four tiers,
      according to its principal business activity. Revenue is a key factor in determining a firm''s principal business activity.
      MSCI and S&P Dow Jones Indices developed this classification standard to provide investors with consistent and exhaustive
      industry definitions.'
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/ClassificationSchemes/IndustrySectorClassificationScheme
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesClassification/GlobalIndustryClassificationStandardsScheme
sources:
- id: fibo-source-6fed3fa3dd
  resource: references/fibo/SEC/Securities/SecuritiesClassification.rdf
  sha256: 6fed3fa3ddd850e875bf020fa5eb79e1d90023fb74888e9c1856e32882bc8f76
  title: FIBO source SEC/Securities/SecuritiesClassification.rdf
title: Global Industry Classification Standards scheme
type: Ontology Individual
---

# Global Industry Classification Standards scheme

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesClassification/GlobalIndustryClassificationStandardsScheme>

## Definition

classification scheme that is a hierarchical four-level system classifying companies based on the principal business activity of the organization

## Annotations

- **label**: Global Industry Classification Standards scheme
- **definition**: classification scheme that is a hierarchical four-level system classifying companies based on the principal business activity of the organization
- **acronym**: GICS
- **adaptedFrom**: https://www.msci.com/our-solutions/indexes/gics
- **explanatoryNote**: The four tiers are: Sectors, Industry Groups, Industries and Sub-Industries. All definitions are standardized and applied to companies globally. Each company is assigned a single GICS classification in each of the four tiers, according to its principal business activity. Revenue is a key factor in determining a firm's principal business activity. MSCI and S&P Dow Jones Indices developed this classification standard to provide investors with consistent and exhaustive industry definitions.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
