---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: common code registry entry
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: entry in a common code registry
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentificationIndividuals/EuroclearClearstreamCommonCode
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/comprises
  - kind: has_value
    property: https://www.omg.org/spec/Commons/Collections/isIncludedIn
    value: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentificationIndividuals/CommonCodeRepository
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/Security
    kind: all_values_from
    property: https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo
  see_also:
  - predicate: http://www.w3.org/2000/01/rdf-schema#seeAlso
    resource: http://www.isin.net/common-code-isin/
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/RegistrationAuthorities/RegistryEntry
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentificationIndividuals/CommonCodeRegistryEntry
sources:
- id: fibo-source-be76358ba2
  resource: references/fibo/SEC/Securities/SecuritiesIdentificationIndividuals.rdf
  sha256: be76358ba2a858eedd6bae77ca133882b7a1e2862cc351839d6b047eb2b024fa
  title: FIBO source SEC/Securities/SecuritiesIdentificationIndividuals.rdf
title: common code registry entry
type: Ontology Class
---

# common code registry entry

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentificationIndividuals/CommonCodeRegistryEntry>

## Definition

entry in a common code registry

## Relationships

- **See also**: [common-code-isin](<http://www.isin.net/common-code-isin/>)
- **Subclass of**: [RegistryEntry](<https://www.omg.org/spec/Commons/RegistrationAuthorities/RegistryEntry>)

## Constraints

- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: some values from of type [EuroclearClearstreamCommonCode](/concepts/fibo/SEC/Securities/SecuritiesIdentificationIndividuals/EuroclearClearstreamCommonCode.md)
- **[isIncludedIn](<https://www.omg.org/spec/Commons/Collections/isIncludedIn>)**: has value value `https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentificationIndividuals/CommonCodeRepository`
- **[appliesTo](<https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo>)**: all values from of type [Security](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/Security.md)

## Annotations

- **label**: common code registry entry
- **definition**: entry in a common code registry

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
