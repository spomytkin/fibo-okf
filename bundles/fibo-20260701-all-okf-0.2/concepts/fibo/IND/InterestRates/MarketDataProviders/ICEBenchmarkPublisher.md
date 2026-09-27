---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: ICE benchmark publisher
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: the ICE Benchmark Administration functional entity that is an international financial information publisher, responsible
      for the publication of ICE LIBOR, ICE Swap Rate, LBMA Gold Price and ISDA SIMM benchmarks
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.theice.com/index
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/InterestRates/InterestRateAuthority
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities/ICEBenchmarkAdministration.md
    predicate: https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/CommercialRegistrationAuthorities/ICEBenchmarkAdministration
resource: https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/MarketDataProviders/ICEBenchmarkPublisher
sources:
- id: fibo-source-0b5fde6ab3
  resource: references/fibo/IND/InterestRates/MarketDataProviders.rdf
  sha256: 0b5fde6ab3fe477e8381e86968420d93073a53e8b18733937a275f845b4e18c4
  title: FIBO source IND/InterestRates/MarketDataProviders.rdf
title: ICE benchmark publisher
type: Ontology Individual
---

# ICE benchmark publisher

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/MarketDataProviders/ICEBenchmarkPublisher>

## Definition

the ICE Benchmark Administration functional entity that is an international financial information publisher, responsible for the publication of ICE LIBOR, ICE Swap Rate, LBMA Gold Price and ISDA SIMM benchmarks

## Relationships

- **Related to**: [ICEBenchmarkAdministration](/concepts/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities/ICEBenchmarkAdministration.md)

## Annotations

- **label**: ICE benchmark publisher
- **definition**: the ICE Benchmark Administration functional entity that is an international financial information publisher, responsible for the publication of ICE LIBOR, ICE Swap Rate, LBMA Gold Price and ISDA SIMM benchmarks
- **adaptedFrom**: https://www.theice.com/index

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
