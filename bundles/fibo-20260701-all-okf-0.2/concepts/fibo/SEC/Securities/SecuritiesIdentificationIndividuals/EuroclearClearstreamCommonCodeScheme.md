---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Euroclear Clearstream common code scheme
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: nine-digit security identification scheme, defined originally by Euroclear and CEDEL (now Clearstream) that is
      used to identify securities in Europe for the purposes of facilitating clearing and settlement of trades
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: http://www.isin.net/common-code-isin/
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: common code scheme
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentification/ProprietarySecurityIdentificationScheme
  related_to:
  - concept: /concepts/fibo/SEC/Securities/SecuritiesIdentificationIndividuals/CommonCodeRepository.md
    predicate: https://www.omg.org/spec/Commons/Designators/describes
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentificationIndividuals/CommonCodeRepository
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentificationIndividuals/EuroclearClearstreamCommonCodeScheme
sources:
- id: fibo-source-be76358ba2
  resource: references/fibo/SEC/Securities/SecuritiesIdentificationIndividuals.rdf
  sha256: be76358ba2a858eedd6bae77ca133882b7a1e2862cc351839d6b047eb2b024fa
  title: FIBO source SEC/Securities/SecuritiesIdentificationIndividuals.rdf
title: Euroclear Clearstream common code scheme
type: Ontology Individual
---

# Euroclear Clearstream common code scheme

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentificationIndividuals/EuroclearClearstreamCommonCodeScheme>

## Definition

nine-digit security identification scheme, defined originally by Euroclear and CEDEL (now Clearstream) that is used to identify securities in Europe for the purposes of facilitating clearing and settlement of trades

## Relationships

- **Related to**: [CommonCodeRepository](/concepts/fibo/SEC/Securities/SecuritiesIdentificationIndividuals/CommonCodeRepository.md)

## Annotations

- **label**: Euroclear Clearstream common code scheme
- **definition**: nine-digit security identification scheme, defined originally by Euroclear and CEDEL (now Clearstream) that is used to identify securities in Europe for the purposes of facilitating clearing and settlement of trades
- **adaptedFrom**: http://www.isin.net/common-code-isin/
- **synonym**: common code scheme

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
