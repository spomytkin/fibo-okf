---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: public offering
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: offering of securities for sale to the investment public, after compliance with registration requirements of the
      relevant regulatory authorities
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: Barron's Dictionary of Finance and Investment Terms, Ninth Edition, 2014.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: In the US, public offerings generally require approval of the Securities Exchange Commission and/or relevant state
      regulators, unless the issuer is an exempt issuer, and are usually conducted by an investment banker or a syndicate
      made up of several investment bankers, at a price agreed upon between the issuer and the investment bankers.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/Prospectus
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/isEvidencedBy
  subclass_of:
  - concept: /concepts/fibo/SEC/Securities/SecuritiesIssuance/SecuritiesOffering.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/SecuritiesOffering
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/PublicOffering
sources:
- id: fibo-source-7b3088e831
  resource: references/fibo/SEC/Securities/SecuritiesIssuance.rdf
  sha256: 7b3088e8315beedb43222e345522bb546f87fbbd6850833103c9ba84ea1d7ac0
  title: FIBO source SEC/Securities/SecuritiesIssuance.rdf
title: public offering
type: Ontology Class
---

# public offering

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/PublicOffering>

## Definition

offering of securities for sale to the investment public, after compliance with registration requirements of the relevant regulatory authorities

## Relationships

- **Subclass of**: [SecuritiesOffering](/concepts/fibo/SEC/Securities/SecuritiesIssuance/SecuritiesOffering.md)

## Constraints

- **[isEvidencedBy](/concepts/fibo/FND/Agreements/Contracts/isEvidencedBy.md)**: some values from of type [Prospectus](/concepts/fibo/SEC/Securities/SecuritiesIssuance/Prospectus.md)

## Annotations

- **label**: public offering
- **definition**: offering of securities for sale to the investment public, after compliance with registration requirements of the relevant regulatory authorities
- **adaptedFrom**: Barron's Dictionary of Finance and Investment Terms, Ninth Edition, 2014.
- **explanatoryNote**: In the US, public offerings generally require approval of the Securities Exchange Commission and/or relevant state regulators, unless the issuer is an exempt issuer, and are usually conducted by an investment banker or a syndicate made up of several investment bankers, at a price agreed upon between the issuer and the investment bankers.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
