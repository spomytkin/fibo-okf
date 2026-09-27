---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: national security identification scheme
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: security identification scheme, defining the format and structure of a National Securities Identifying Number (NSIN),
      published nationally on behalf of a country
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: generally incorporated into the ISIN scheme as well
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://www.omg.org/spec/Commons/Locations/GeopoliticalEntity
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentification/NationalSecuritiesIdentifyingNumber
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Designators/defines
  subclass_of:
  - concept: /concepts/fibo/SEC/Securities/SecuritiesIdentification/SecurityIdentificationScheme.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentification/SecurityIdentificationScheme
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentification/NationalSecurityIdentificationScheme
sources:
- id: fibo-source-966091c50a
  resource: references/fibo/SEC/Securities/SecuritiesIdentification.rdf
  sha256: 966091c50a68aae0becec1ae82b25a9fa7129356c4caa9b25ba1ed33b8fdd2cf
  title: FIBO source SEC/Securities/SecuritiesIdentification.rdf
title: national security identification scheme
type: Ontology Class
---

# national security identification scheme

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentification/NationalSecurityIdentificationScheme>

## Definition

security identification scheme, defining the format and structure of a National Securities Identifying Number (NSIN), published nationally on behalf of a country

## Relationships

- **Subclass of**: [SecurityIdentificationScheme](/concepts/fibo/SEC/Securities/SecuritiesIdentification/SecurityIdentificationScheme.md)

## Constraints

- **[appliesTo](<https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo>)**: some values from of type [GeopoliticalEntity](<https://www.omg.org/spec/Commons/Locations/GeopoliticalEntity>)
- **[defines](<https://www.omg.org/spec/Commons/Designators/defines>)**: some values from of type [NationalSecuritiesIdentifyingNumber](/concepts/fibo/SEC/Securities/SecuritiesIdentification/NationalSecuritiesIdentifyingNumber.md)

## Annotations

- **label**: national security identification scheme
- **definition**: security identification scheme, defining the format and structure of a National Securities Identifying Number (NSIN), published nationally on behalf of a country
- **explanatoryNote**: generally incorporated into the ISIN scheme as well

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
