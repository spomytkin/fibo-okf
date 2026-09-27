---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: CGS CUSIP Access Repository
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: CGS (CUSIP Global Services) CUSIP Access services and repository, a proprietary repository of security identifiers,
      issued by CUSIP Global Services, that is the National Securities Identifying Number (NSIN) for securities issued in
      North America, which is also part of the ISIN for the security it identifies
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentification/NationalSecuritiesIdentifyingNumberRegistry
  related_to:
  - concept: /concepts/fibo/SEC/Securities/SecuritiesIdentificationIndividuals/CUSIPGlobalServices.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentificationIndividuals/CUSIPGlobalServices
  see_also:
  - predicate: http://www.w3.org/2000/01/rdf-schema#seeAlso
    resource: https://www.cusip.com/cusip/index.htm
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentificationIndividuals/CGSCUSIPAccessRepository
sources:
- id: fibo-source-be76358ba2
  resource: references/fibo/SEC/Securities/SecuritiesIdentificationIndividuals.rdf
  sha256: be76358ba2a858eedd6bae77ca133882b7a1e2862cc351839d6b047eb2b024fa
  title: FIBO source SEC/Securities/SecuritiesIdentificationIndividuals.rdf
title: CGS CUSIP Access Repository
type: Ontology Individual
---

# CGS CUSIP Access Repository

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentificationIndividuals/CGSCUSIPAccessRepository>

## Definition

CGS (CUSIP Global Services) CUSIP Access services and repository, a proprietary repository of security identifiers, issued by CUSIP Global Services, that is the National Securities Identifying Number (NSIN) for securities issued in North America, which is also part of the ISIN for the security it identifies

## Relationships

- **Related to**: [CUSIPGlobalServices](/concepts/fibo/SEC/Securities/SecuritiesIdentificationIndividuals/CUSIPGlobalServices.md)
- **See also**: [index.htm](<https://www.cusip.com/cusip/index.htm>)

## Annotations

- **label**: CGS CUSIP Access Repository
- **definition**: CGS (CUSIP Global Services) CUSIP Access services and repository, a proprietary repository of security identifiers, issued by CUSIP Global Services, that is the National Securities Identifying Number (NSIN) for securities issued in North America, which is also part of the ISIN for the security it identifies

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
