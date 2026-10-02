---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: blue sky law
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: state-level securities regulation, designed to protect investors against securities fraud that require issuers
      to be registered and to disclose details of their offerings
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: This allows investors to base their judgments on trustworthy data.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/usageNote
    value: Blue sky law is modeled as a class, rather than as a named individual, because there are numerous state-specific
      laws that qualify as blue sky laws that could be added to support state-specific definitions and other analyses.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://www.omg.org/spec/Commons/Locations/GeographicRegion
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/ContextualDesignators/isApplicableIn
  subclass_of:
  - concept: /concepts/fibo/SEC/Securities/SecuritiesRestrictions/SecuritiesRegulation.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesRestrictions/SecuritiesRegulation
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/NorthAmericanSecurities/USSecuritiesRestrictions/BlueSkyLaw
sources:
- id: fibo-source-91c51c4810
  resource: references/fibo/SEC/Securities/NorthAmericanSecurities/USSecuritiesRestrictions.rdf
  sha256: 91c51c4810cfe6c5acc0aaf99de529357298d47f01cfe4f5eee4962f40f5be33
  title: FIBO source SEC/Securities/NorthAmericanSecurities/USSecuritiesRestrictions.rdf
title: blue sky law
type: Ontology Class
---

# blue sky law

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/NorthAmericanSecurities/USSecuritiesRestrictions/BlueSkyLaw>

## Definition

state-level securities regulation, designed to protect investors against securities fraud that require issuers to be registered and to disclose details of their offerings

## Relationships

- **Subclass of**: [SecuritiesRegulation](/concepts/fibo/SEC/Securities/SecuritiesRestrictions/SecuritiesRegulation.md)

## Constraints

- **[isApplicableIn](<https://www.omg.org/spec/Commons/ContextualDesignators/isApplicableIn>)**: min qualified cardinality 0 of type [GeographicRegion](<https://www.omg.org/spec/Commons/Locations/GeographicRegion>)

## Annotations

- **label**: blue sky law
- **definition**: state-level securities regulation, designed to protect investors against securities fraud that require issuers to be registered and to disclose details of their offerings
- **explanatoryNote**: This allows investors to base their judgments on trustworthy data.
- **usageNote**: Blue sky law is modeled as a class, rather than as a named individual, because there are numerous state-specific laws that qualify as blue sky laws that could be added to support state-specific definitions and other analyses.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
