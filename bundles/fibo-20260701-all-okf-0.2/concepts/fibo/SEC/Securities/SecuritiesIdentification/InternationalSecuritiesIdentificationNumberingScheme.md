---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: international securities identification numbering scheme
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: formal definition of the structure and application of a ISINs as defined in ISO 6166
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: ISIN scheme
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentification/InternationalSecuritiesIdentificationNumber
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Designators/defines
  see_also:
  - predicate: http://www.w3.org/2000/01/rdf-schema#seeAlso
    resource: http://www.iso.org/iso/catalogue_detail?csnumber=44811
  subclass_of:
  - concept: /concepts/fibo/SEC/Securities/SecuritiesIdentification/SecurityIdentificationScheme.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentification/SecurityIdentificationScheme
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentification/InternationalSecuritiesIdentificationNumberingScheme
sources:
- id: fibo-source-966091c50a
  resource: references/fibo/SEC/Securities/SecuritiesIdentification.rdf
  sha256: 966091c50a68aae0becec1ae82b25a9fa7129356c4caa9b25ba1ed33b8fdd2cf
  title: FIBO source SEC/Securities/SecuritiesIdentification.rdf
title: international securities identification numbering scheme
type: Ontology Class
---

# international securities identification numbering scheme

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentification/InternationalSecuritiesIdentificationNumberingScheme>

## Definition

formal definition of the structure and application of a ISINs as defined in ISO 6166

## Relationships

- **See also**: [catalogue_detail](<http://www.iso.org/iso/catalogue_detail?csnumber=44811>)
- **Subclass of**: [SecurityIdentificationScheme](/concepts/fibo/SEC/Securities/SecuritiesIdentification/SecurityIdentificationScheme.md)

## Constraints

- **[defines](<https://www.omg.org/spec/Commons/Designators/defines>)**: some values from of type [InternationalSecuritiesIdentificationNumber](/concepts/fibo/SEC/Securities/SecuritiesIdentification/InternationalSecuritiesIdentificationNumber.md)

## Annotations

- **label**: international securities identification numbering scheme
- **definition**: formal definition of the structure and application of a ISINs as defined in ISO 6166
- **abbreviation**: ISIN scheme

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
