---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Financial Instrument Global Identifier (FIGI) Registry
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: open, OMG standards-based registry used by the FIGI registration authority to manage the financial instrument identifiers
      and related information that it registers according to the Financial Instrument Global Identifier (FIGI) standard
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: FIGI Registry
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.omg.org/spec/FIGI
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://www.omg.org/spec/Commons/RegistrationAuthorities/Registry
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities/BloombergLP.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/CommercialRegistrationAuthorities/BloombergLP
  see_also:
  - predicate: http://www.w3.org/2000/01/rdf-schema#seeAlso
    resource: http://www.openfigi.com/
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentificationIndividuals/FinancialInstrumentGlobalIdentifierRegistry
sources:
- id: fibo-source-be76358ba2
  resource: references/fibo/SEC/Securities/SecuritiesIdentificationIndividuals.rdf
  sha256: be76358ba2a858eedd6bae77ca133882b7a1e2862cc351839d6b047eb2b024fa
  title: FIBO source SEC/Securities/SecuritiesIdentificationIndividuals.rdf
title: Financial Instrument Global Identifier (FIGI) Registry
type: Ontology Individual
---

# Financial Instrument Global Identifier (FIGI) Registry

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentificationIndividuals/FinancialInstrumentGlobalIdentifierRegistry>

## Definition

open, OMG standards-based registry used by the FIGI registration authority to manage the financial instrument identifiers and related information that it registers according to the Financial Instrument Global Identifier (FIGI) standard

## Relationships

- **Related to**: [BloombergLP](/concepts/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities/BloombergLP.md)
- **See also**: [http://www.openfigi.com/](<http://www.openfigi.com/>)

## Annotations

- **label**: Financial Instrument Global Identifier (FIGI) Registry
- **definition**: open, OMG standards-based registry used by the FIGI registration authority to manage the financial instrument identifiers and related information that it registers according to the Financial Instrument Global Identifier (FIGI) standard
- **abbreviation**: FIGI Registry
- **adaptedFrom**: https://www.omg.org/spec/FIGI

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
