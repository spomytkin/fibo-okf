---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: prospectus
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: http://www.w3.org/2000/01/rdf-schema#seeAlso
    value: http://www.investopedia.com/terms/p/prospectus.asp
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: formal, written offering document to sell securities that provides the facts an investor needs to make an informed
      investment decision
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#editorialNote
    value: 'EFAMA Review description for this: The fund is issued with a prospectus; there is material in the prospectus that
      is binding; material that is expected but not binding, and information that may or may not be in the prospectus or a
      given fund.'
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: Barron's Dictionary of Finance and Investment Terms, Ninth Edition, 2014.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: The Securities Act of 1933, as amended 5 April 2012, see http://www.sec.gov/about/laws/sa33.pdf
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A prospectus may specify the facts about an offering of securities, mutual funds, or limited partnerships for investments
      in oil, gas, equipment leasing, or other kinds of limited partnerships.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: In the United States, a prospectus may be a formal legal document, required by and filed with the Securities and
      Exchange Commission, if it provides details about an investment offering for sale to the public.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: This document includes facts about the fund investment objective, investment focus and other details of the fund.
      Some of this information becomes binding on the fund once it is issued, while other information is guidelines only.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/FundInvestmentObjective
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/outlines
  subclass_of:
  - concept: /concepts/fibo/SEC/Securities/SecuritiesIssuance/OfferingDocument.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/OfferingDocument
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/Prospectus
sources:
- id: fibo-source-ee709790f7
  resource: references/fibo/SEC/Funds/CollectiveInvestmentVehicles.rdf
  sha256: ee709790f7157eacba64b78b55ac3e69da45c99673be17ca2df35d4f0ed3230c
  title: FIBO source SEC/Funds/CollectiveInvestmentVehicles.rdf
- id: fibo-source-7b3088e831
  resource: references/fibo/SEC/Securities/SecuritiesIssuance.rdf
  sha256: 7b3088e8315beedb43222e345522bb546f87fbbd6850833103c9ba84ea1d7ac0
  title: FIBO source SEC/Securities/SecuritiesIssuance.rdf
title: prospectus
type: Ontology Class
---

# prospectus

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/Prospectus>

## Definition

formal, written offering document to sell securities that provides the facts an investor needs to make an informed investment decision

## Relationships

- **Subclass of**: [OfferingDocument](/concepts/fibo/SEC/Securities/SecuritiesIssuance/OfferingDocument.md)

## Constraints

- **[outlines](/concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/outlines.md)**: some values from of type [FundInvestmentObjective](/concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/FundInvestmentObjective.md)

## Annotations

- **label**: prospectus
- **seeAlso**: http://www.investopedia.com/terms/p/prospectus.asp
- **definition**: formal, written offering document to sell securities that provides the facts an investor needs to make an informed investment decision
- **editorialNote** (en): EFAMA Review description for this: The fund is issued with a prospectus; there is material in the prospectus that is binding; material that is expected but not binding, and information that may or may not be in the prospectus or a given fund.
- **adaptedFrom**: Barron's Dictionary of Finance and Investment Terms, Ninth Edition, 2014.
- **adaptedFrom**: The Securities Act of 1933, as amended 5 April 2012, see http://www.sec.gov/about/laws/sa33.pdf
- **explanatoryNote**: A prospectus may specify the facts about an offering of securities, mutual funds, or limited partnerships for investments in oil, gas, equipment leasing, or other kinds of limited partnerships.
- **explanatoryNote**: In the United States, a prospectus may be a formal legal document, required by and filed with the Securities and Exchange Commission, if it provides details about an investment offering for sale to the public.
- **explanatoryNote**: This document includes facts about the fund investment objective, investment focus and other details of the fund. Some of this information becomes binding on the fund once it is issued, while other information is guidelines only.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
