---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: common code repository
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: distributed international repository of security identifiers, issued by Euroclear or Clearstream (CEDEL), that
      are used to identify securities in Europe for the purposes of facilitating clearing and settlement of trades
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: http://www.isin.net/common-code-isin/
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://www.omg.org/spec/Commons/RegistrationAuthorities/Registry
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities/Clearstream.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/CommercialRegistrationAuthorities/Clearstream
  see_also:
  - predicate: http://www.w3.org/2000/01/rdf-schema#seeAlso
    resource: http://www.isin.net/common-code-isin/
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentificationIndividuals/CommonCodeRepository
sources:
- id: fibo-source-be76358ba2
  resource: references/fibo/SEC/Securities/SecuritiesIdentificationIndividuals.rdf
  sha256: be76358ba2a858eedd6bae77ca133882b7a1e2862cc351839d6b047eb2b024fa
  title: FIBO source SEC/Securities/SecuritiesIdentificationIndividuals.rdf
title: common code repository
type: Ontology Individual
---

# common code repository

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentificationIndividuals/CommonCodeRepository>

## Definition

distributed international repository of security identifiers, issued by Euroclear or Clearstream (CEDEL), that are used to identify securities in Europe for the purposes of facilitating clearing and settlement of trades

## Relationships

- **Related to**: [Clearstream](/concepts/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities/Clearstream.md)
- **See also**: [common-code-isin](<http://www.isin.net/common-code-isin/>)

## Annotations

- **label**: common code repository
- **definition**: distributed international repository of security identifiers, issued by Euroclear or Clearstream (CEDEL), that are used to identify securities in Europe for the purposes of facilitating clearing and settlement of trades
- **adaptedFrom**: http://www.isin.net/common-code-isin/

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
