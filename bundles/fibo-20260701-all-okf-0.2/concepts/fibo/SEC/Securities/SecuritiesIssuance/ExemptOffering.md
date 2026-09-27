---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: exempt offering
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: public offering involving securities that are excused from certain regulatory reporting requirements
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: Barron's Dictionary of Finance and Investment Terms, Ninth Edition, 2014.
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: http://www.investopedia.com/exam-guide/series-66/regulation-of-securities/exempt-securities.asp
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Such an offering may be considered exempt either because the issuer is exempt or the transaction specific to the
      offering is exempt.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/SEC/Securities/SecuritiesIssuance/PublicOffering.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/PublicOffering
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/ExemptOffering
sources:
- id: fibo-source-7b3088e831
  resource: references/fibo/SEC/Securities/SecuritiesIssuance.rdf
  sha256: 7b3088e8315beedb43222e345522bb546f87fbbd6850833103c9ba84ea1d7ac0
  title: FIBO source SEC/Securities/SecuritiesIssuance.rdf
title: exempt offering
type: Ontology Class
---

# exempt offering

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/ExemptOffering>

## Definition

public offering involving securities that are excused from certain regulatory reporting requirements

## Relationships

- **Subclass of**: [PublicOffering](/concepts/fibo/SEC/Securities/SecuritiesIssuance/PublicOffering.md)

## Annotations

- **label**: exempt offering
- **definition**: public offering involving securities that are excused from certain regulatory reporting requirements
- **adaptedFrom**: Barron's Dictionary of Finance and Investment Terms, Ninth Edition, 2014.
- **adaptedFrom**: http://www.investopedia.com/exam-guide/series-66/regulation-of-securities/exempt-securities.asp
- **explanatoryNote**: Such an offering may be considered exempt either because the issuer is exempt or the transaction specific to the offering is exempt.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
