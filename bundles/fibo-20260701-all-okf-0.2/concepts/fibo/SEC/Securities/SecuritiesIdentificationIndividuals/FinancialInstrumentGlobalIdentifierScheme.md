---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: financial instrument global identifier scheme
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: standard identification scheme for financial instrument identifiers (not limited to securities) and, in some cases,
      related listings, published by the Object Management Group (OMG)
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: FIGI scheme
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.omg.org/spec/FIGI
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentification/FinancialInstrumentIdentificationScheme
  - https://www.omg.org/spec/Commons/RegistrationAuthorities/RegistrationScheme
  related_to:
  - concept: /concepts/fibo/SEC/Securities/SecuritiesIdentificationIndividuals/FinancialInstrumentGlobalIdentifierRegistry.md
    predicate: https://www.omg.org/spec/Commons/Designators/describes
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentificationIndividuals/FinancialInstrumentGlobalIdentifierRegistry
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentificationIndividuals/FinancialInstrumentGlobalIdentifierScheme
sources:
- id: fibo-source-be76358ba2
  resource: references/fibo/SEC/Securities/SecuritiesIdentificationIndividuals.rdf
  sha256: be76358ba2a858eedd6bae77ca133882b7a1e2862cc351839d6b047eb2b024fa
  title: FIBO source SEC/Securities/SecuritiesIdentificationIndividuals.rdf
title: financial instrument global identifier scheme
type: Ontology Individual
---

# financial instrument global identifier scheme

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentificationIndividuals/FinancialInstrumentGlobalIdentifierScheme>

## Definition

standard identification scheme for financial instrument identifiers (not limited to securities) and, in some cases, related listings, published by the Object Management Group (OMG)

## Relationships

- **Related to**: [FinancialInstrumentGlobalIdentifierRegistry](/concepts/fibo/SEC/Securities/SecuritiesIdentificationIndividuals/FinancialInstrumentGlobalIdentifierRegistry.md)

## Annotations

- **label**: financial instrument global identifier scheme
- **definition**: standard identification scheme for financial instrument identifiers (not limited to securities) and, in some cases, related listings, published by the Object Management Group (OMG)
- **abbreviation**: FIGI scheme
- **adaptedFrom**: https://www.omg.org/spec/FIGI

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
